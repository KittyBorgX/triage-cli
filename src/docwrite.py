from datetime import datetime
import os
from conf import backup_dir, backup

class DocumentWriter:
    def __init__(self):
        self.sorted_pull_requests = {}
        self.cont_str = ""
        self.report = []
        self.d = None

    def parse_date(self, date: str):
        d = date.split("T")[0]
        t = date.split("T")[1].split("Z")[0]
        return f"{d} Time: {t}"

    def register_type(self, label):
        self.label = "# " + label + "\n"

    def add_pull_request(self, pr_number: int, author: str, reviewer: str, status: str, details: list = None):
        if reviewer not in self.sorted_pull_requests:
            self.sorted_pull_requests[reviewer] = []
        self.sorted_pull_requests[reviewer].append(
            (pr_number, author, status))

        if details is not None:
            self.d = details
            self.t = details[0]
            self.m = details[1]
            self.l = details[2]
            self.c = details[3]
            self.me = details[4]

        self.get_sorted_pull_requests()

    def get_sorted_pull_requests(self) -> str:
        sorted_reviewers = sorted(self.sorted_pull_requests.keys())
        report = []
        report += self.label
        for reviewer in sorted_reviewers:
            pull_requests = self.sorted_pull_requests[reviewer]
            pull_requests.sort(key=lambda x: x[0])
            if self.d is not None:
                pull_requests_str = "\n".join(
                    [f"- #{pr_number} - {status} - author: {author}\n{self.details(self.t, self.m, self.l, self.c, self.me)}" for pr_number, author, status in pull_requests])
            else:
                pull_requests_str = "\n".join(
                    [f"- #{pr_number} - {status} - author: {author}\n" for pr_number, author, status in pull_requests])
            report.append(f"\n### {reviewer}\n{pull_requests_str}\n")
        self.report = report
        return "".join(report)

    def get_report(self):
        return "".join(self.report)

    def details(self, t, d, l, c, me):
        out_str = ""
        out_str += "\t<details>\n\t<summary>Details - Click Me </summary>\n\n"
        out_str += f"\tTitle: {t}\n\n"
        out_str += f"\tLast Updated at: {self.parse_date(d)}\n\n"
        out_str += f"\tCreated at: {self.parse_date(c)}\n\n"
        out_str += f"\tLabels: "
        for i in l:
            out_str += f"{i}, "
        out_str += "\n\n"
        out_str += f"\tStatus: {str(me).lower()}\n\n"
        out_str += f"\t</details>\n\n"

        return out_str

    def write(self):
        if backup():
            filename = str(backup_dir()) + \
                str(datetime.now()).split(" ")[0] + ".md"
            if os.path.exists:
                with open(filename, "+w") as f:
                    f.write("".join(self.report))
            else:
                with open(filename, "+x") as f:
                    f.write("".join(self.report))
