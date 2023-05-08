class PullRequestSorter:
    def __init__(self):
        self.sorted_pull_requests = {}

    def add_pull_request(self, pr_number: int, author: str, reviewer: str, status: str):
        if reviewer not in self.sorted_pull_requests:
            self.sorted_pull_requests[reviewer] = []
        self.sorted_pull_requests[reviewer].append((pr_number, author, status))

    def get_sorted_pull_requests(self) -> str:
        sorted_reviewers = sorted(self.sorted_pull_requests.keys())
        report = []
        for reviewer in sorted_reviewers:
            pull_requests = self.sorted_pull_requests[reviewer]
            pull_requests.sort(key=lambda x: x[0])
            pull_requests_str = "\n".join(
                [f"- #{pr_number} - {status} - author: {author}" for pr_number, author, status in pull_requests])
            report.append(f"\n### {reviewer}\n{pull_requests_str}")
        return "".join(report)
