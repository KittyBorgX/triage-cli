from http import HTTPStatus
import httpx
from conf import gh_token


class GitHubGraphQLClient:
    def __init__(self):
        self.token = gh_token()
        self.endpoint = "https://api.github.com/graphql"
        self.headers = {"Authorization": f"Bearer {self.token}"}

    async def get_pull_request(self, pr_num: int) -> dict:
        query = """
        query ($owner: String!, $repo: String!, $number: Int!) {
            repository(owner: $owner, name: $repo) {
                pullRequest(number: $number) {
                    number
                    title
                    closed
                    author {
                        login
                    }
                    assignees(first: 1) {
                        nodes {
                            login
                        }
                    }
                    createdAt
                    updatedAt
                    mergeable
                    headRefName
                    baseRefName
                    reviews(last: 1) {
                        nodes {
                            author {
                                login
                            }
                            state
                        }
                    }
                    labels(first: 100) {
                        nodes {
                            name
                        }
                    }
                }
            }
        }
        """

        variables = {"owner": "rust-lang", "repo": "rust", "number": pr_num}
        response = await self._send_request(query, variables)

        if response.status_code != HTTPStatus.OK:
            raise Exception(
                f"Failed to retrieve pull request {pr_num}. Error: {response.text}")

        data = response.json()
        pull_request = data.get("data", {}).get(
            "repository", {}).get("pullRequest")

        if not pull_request:
            raise Exception(f"Pull request {pr_num} not found.")

        if pull_request.get("closed"):
            raise Exception(
                f"Pull request {pr_num} is closed and cannot be triaged.")
        print(type(pull_request))
        self.pr_data = pull_request
        return pull_request

    def _send_request(self, query: str, variables: dict) -> httpx.Response:
        response = httpx.post(
            self.endpoint,
            headers=self.headers,
            json={"query": query, "variables": variables},
        )

        return response

    async def get_author(self, pr: int):
        x = await self.get_pull_request(pr)
        return x['author']['login']

    async def get_reviewer(self, pr: int):
        x = await self.get_pull_request(pr)
        return x["assignees"]["nodes"][0]["login"] if x["assignees"]["nodes"] else None

    async def last_updated_date(self, pr: int):
        return self.get_pull_request(pr)['updatedAt']
