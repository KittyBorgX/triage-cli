import httpx
from conf import zulip_email, zulip_token
from error import Error


class ZulipApi:
    def __init__(self) -> None:
        self.post_url = "https://rust-lang.zulipchat.com/api/v1/messages"

    def post(self, topic, content):
        req = {
            "type": "stream",
            "to": "242269",
            "topic": topic,
            "content": content,
        }

        httpx.post(self.post_url, data=req,
                       auth=(zulip_email(), zulip_token()))
        Error(
            f"note: posted the report to zulip in the topic name {topic}", False)
        