import asyncio
from datetime import datetime
from docwrite import DocumentWriter
from api import GitHubGraphQLClient


async def main():
    doc = DocumentWriter()
    doc.register_type("S-waiting-on-review")

    # TODO: Make this available as args after argparse is introduced
    extra = input(
        "Add additional details to the pull requests? [Y/n] (Default: No): ")

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
        pr_obj = GitHubGraphQLClient(pr_number)
        author = pr_obj.get_author()
        reviewer = pr_obj.get_reviewer()

        if extra.lower() == 'y':
            doc.add_pull_request(
                pr_number, author, reviewer, status, [pr_obj.get_title(), pr_obj.last_updated_date(), pr_obj.labels(), pr_obj.created_date()])
        else:
            doc.add_pull_request(
                pr_number, author, reviewer, status)
        print()

    spr = doc.get_report()

    zulip_post = input("Post the report to zulip? [Y/n] (Default: No)")
    if zulip_post.lower() == 'y':
        topic_name = str(datetime.now()).split(" ")[0]
        from zulip import ZulipApi
        zulipobj = ZulipApi()
        zulipobj.post(topic_name, spr)

    print(spr)
    doc.write()

asyncio.run(main())
