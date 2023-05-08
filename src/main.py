import asyncio
from docwrite import PullRequestSorter
from api import GitHubGraphQLClient


async def main():
    graphqlAPI = GitHubGraphQLClient()
    pull_request_sorter = PullRequestSorter()
    pull_request_sorter.register_type("S-waiting-on-review")
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

        author = await graphqlAPI.get_author(pr_number)
        reviewer = await graphqlAPI.get_reviewer(pr_number)

        pull_request_sorter.add_pull_request(
            pr_number, author, reviewer, status)

        print()

    sorted_pull_requests = pull_request_sorter.get_sorted_pull_requests()

    print(sorted_pull_requests)
    pull_request_sorter.write()
asyncio.run(main())
