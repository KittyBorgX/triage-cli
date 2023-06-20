import asyncio
from datetime import datetime
from docwrite import DocumentWriter
from api import GitHubGraphQLClient
from cli import CLIParser
from conf import check_env_vars


def main():
    check_env_vars()
    doc = DocumentWriter()
    cli_parser = CLIParser()
    doc.register_type("S-waiting-on-review")

    if cli_parser.has_arg("-h") or cli_parser.has_arg("--help"):
        cli_parser.help()
        exit(0)

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

        if cli_parser.has_arg("-d") or cli_parser.has_arg("--details"):
            doc.add_pull_request(
                pr_number, author, reviewer, status, [pr_obj.get_title(), pr_obj.last_updated_date(), pr_obj.labels(), pr_obj.created_date(), pr_obj.mergeable()])
        else:
            doc.add_pull_request(
                pr_number, author, reviewer, status)
        print()

    spr = doc.get_report()

    if cli_parser.has_arg("--post-to-zulip") or cli_parser.has_arg("-pz"):
        topic_name = str(datetime.now()).split(" ")[0]
        from zulip import ZulipApi
        zulipobj = ZulipApi()
        zulipobj.post(topic_name, spr)

    if cli_parser.has_arg("-p") or cli_parser.has_arg("--print"):
        print(spr)

    if cli_parser.has_arg("-o") or cli_parser.has_arg("--output"):
        doc.write()


main()
