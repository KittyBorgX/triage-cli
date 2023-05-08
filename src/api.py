import httpx
from typing import List


class GitHubAPI:
    def __init__(self, owner: str, repo: str):
        self.owner = owner
        self.repo = repo
        # self.token = token
        self.base_url = f"https://api.github.com/repos/{self.owner}/{self.repo}"

    async def get_pull_request(self, pr_number: int) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/pulls/{pr_number}", headers={"User-Agent": "request"})

            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(
                    f"Failed to get pull request. Response status code: {response.status_code}")

    async def get_pull_requests(self, state: str = "open") -> List[dict]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/pulls?state={state}")
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(
                    f"Failed to get pull requests. Response status code: {response.status_code}")

    async def get_author(self, pr_num: int):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/pulls/{pr_num}", headers={"Accept": "application/vnd.github.v3+json"})
            print("------------------------------------------------------------")
            print(response)
            print("------------------------------------------------------------")
            jsonobj = response.json()["user"]["login"]
            return jsonobj

    async def get_reviewer(self, pr_num: int):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/pulls/{pr_num}", headers={"User-Agent": "request"})
            jsonobj = response.json()["assignee"]["login"]
            return jsonobj

    async def last_updated_date(self, pr_num: int):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/pulls/{pr_num}", headers={"User-Agent": "request"})
            jsonobj = response.json()["updated_at"]
            return jsonobj
