import asyncio
import datetime
from api import GitHubAPI
from document_writer import DocumentWriter
from sort import PullRequestSorter
from graphql_api import GitHubGraphQLClient


async def main():
    owner = "rust-lang"
    repo = "rust"

    api = GitHubAPI(owner, repo)
    graphqlAPI = GitHubGraphQLClient()

    pull_request_sorter = PullRequestSorter()

    while True:
        pr_number = input("PR num > ")
        if pr_number == "q":
            break
        try:
            pr_number = int(pr_number)
        except ValueError:
            print("Invalid PR number. Please enter a valid PR number or q to quit.")
            continue
        status = input("Status > ")

        author = graphqlAPI.get_author(pr_number)
        reviewer = graphqlAPI.get_reviewer(pr_number)
        date = graphqlAPI.last_updated_date(pr_number)

        dt = datetime.datetime.strptime(
            date,
            "%Y-%m-%dT%H:%M:%SZ"
        )
        pull_request_sorter.add_pull_request(
            pr_number, author, reviewer, status)

        print()

    sorted_pull_requests = pull_request_sorter.get_sorted_pull_requests()

    print(sorted_pull_requests)

asyncio.run(main())
