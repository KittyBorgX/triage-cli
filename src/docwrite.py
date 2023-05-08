from datetime import datetime
from conf import backup_dir, backup


class PullRequestSorter:
    def __init__(self):
        self.sorted_pull_requests = {}
        self.cont_str = ""
        self.report = []

    def register_type(self, label):
        self.label = "# " + label + "\n"

    def add_pull_request(self, pr_number: int, author: str, reviewer: str, status: str):
        if reviewer not in self.sorted_pull_requests:
            self.sorted_pull_requests[reviewer] = []
        self.sorted_pull_requests[reviewer].append((pr_number, author, status))

    def get_sorted_pull_requests(self) -> str:
        sorted_reviewers = sorted(self.sorted_pull_requests.keys())
        report = []
        report += self.label
        for reviewer in sorted_reviewers:
            pull_requests = self.sorted_pull_requests[reviewer]
            pull_requests.sort(key=lambda x: x[0])
            pull_requests_str = "\n".join(
                [f"- #{pr_number} - {status} - author: {author}" for pr_number, author, status in pull_requests])
            report.append(f"\n### {reviewer}\n{pull_requests_str}\n")
        self.report = report
        return "".join(report)

    def write(self):
        if backup():
            filename = str(backup_dir()) + \
                str(datetime.now()).split(" ")[0] + ".md"
            with open(filename, "+x") as f:
                f.write("".join(self.report))
