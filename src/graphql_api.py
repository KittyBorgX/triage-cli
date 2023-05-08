import os
from http import HTTPStatus

import httpx


class GitHubGraphQLClient:
    def __init__(self):
        self.token = os.getenv("GITHUB_ACCESS_TOKEN")
        self.endpoint = "https://api.github.com/graphql"
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def get_pull_request(self, pr_num: int) -> dict:
        query = """
        query ($owner: String!, $repo: String!, $number: Int!) {
            repository(owner: $owner, name: $repo) {
                pullRequest(number: $number) {
                    number
                    title
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
        response = self._send_request(query, variables)

        if response.status_code != HTTPStatus.OK:
            raise Exception(
                f"Failed to retrieve pull request {pr_num}. Error: {response.text}")

        data = response.json()
        pull_request = data.get("data", {}).get(
            "repository", {}).get("pullRequest")

        if not pull_request:
            raise Exception(f"Pull request {pr_num} not found.")

        return pull_request

    def _send_request(self, query: str, variables: dict) -> httpx.Response:
        response = httpx.post(
            self.endpoint,
            headers=self.headers,
            json={"query": query, "variables": variables},
        )

        return response

    def get_author(self, pr: int):
        return self.get_pull_request(pr)['author']['login']

    def get_reviewer(self, pr: int):
        return self.get_pull_request(pr)["assignees"]["nodes"][0]["login"] if self.get_pull_request(pr)["assignees"]["nodes"] else None

    def last_updated_date(self, pr: int):
        return self.get_pull_request(pr)['updatedAt']