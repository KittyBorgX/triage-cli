import os
from dotenv import load_dotenv
from error import Error


def backup():
    load_dotenv()
    if os.getenv("TCLI_BACKUP_DIR") is None:
        return False
    else:
        return True


def backup_dir():
    load_dotenv()
    if backup():
        p = os.getenv("TCLI_BACKUP_DIR")
        if not os.path.exists(p):
            os.makedirs(p)
        return os.getenv("TCLI_BACKUP_DIR")
    else:
        return


def gh_token():
    load_dotenv()
    if os.getenv("GITHUB_ACCESS_TOKEN") is None:
        Error("error: There is no github token set", False)
        Error(
            "note: Please set one in the .env file or set the $GITHUB_ACCESS_TOKEN environment variable")
    else:
        return os.getenv("GITHUB_ACCESS_TOKEN")


def zulip_token():
    load_dotenv()

    if os.getenv("ZULIP_API_KEY") is None:
        Error("error: There is no zulip api key set", False)
        Error(
            "note: Please set one in the .env file or set the $ZULIP_API_KEY environment variable")

    else:
        return os.getenv("ZULIP_API_KEY")


def zulip_email():
    load_dotenv()

    if os.getenv("ZULIP_EMAIL_ID") is None:
        Error("error: There is no zulip email id set")
        Error(
            "note: Please set one in the .env file or set the $ZULIP_EMAIL_ID environment variable")
    else:
        return os.getenv("ZULIP_API_KEY")


def check_env_vars():
    gh_token()
