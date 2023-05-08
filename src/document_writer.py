from datetime import datetime, timedelta
from typing import List


class DocumentWriter:
    def __init__(self):
        self.reports = {}

    def add_pull_request(self, pr_number: int, author: str, reviewer: str, status: str, last_updated: datetime):
        month_ago = datetime.now() - timedelta(days=30)
        if last_updated < month_ago:
            if reviewer not in self.reports:
                self.reports[reviewer] = []
            self.reports[reviewer].append((pr_number, author, status))

    def generate_report(self) -> str:
        report = ""
        for reviewer, pr_list in self.reports.items():
            report += f"\n### {reviewer}\n"
            for pr_number, author, status in pr_list:
                report += f"- #{pr_number} - {status} - author: {author}\n"
        if report:
            return f"# S-waiting-on-review{report}\n"
        else:
            return ""
