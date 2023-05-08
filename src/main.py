import asyncio
from datetime import datetime
from docwrite import DocumentWriter
from api import GitHubGraphQLClient


async def main():
    api = GitHubGraphQLClient()
    doc = DocumentWriter()
    doc.register_type("S-waiting-on-review")
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

        author = await api.get_author(pr_number)
        reviewer = await api.get_reviewer(pr_number)

        doc.add_pull_request(
            pr_number, author, reviewer, status)

        print()

    sorted_pull_requests = doc.get_sorted_pull_requests()

    zulip_post = input("Post the report to zulip? [Y/n] (Default: No)")
    if zulip_post.lower() == 'y':
        topic_name = str(datetime.now()).split(" ")[0]
        from zulip import ZulipApi
        zulipobj = ZulipApi()
        zulipobj.post(topic_name, sorted_pull_requests)

    print(sorted_pull_requests)
    doc.write()

asyncio.run(main())
