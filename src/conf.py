import os
from dotenv import load_dotenv


def backup():
    load_dotenv()
    if len(os.getenv("TCLI_BACKUP_DIR")) == 0:
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
    if len(os.getenv("GITHUB_ACCESS_TOKEN")) == 0:
        print("error: There is no github token set")
        print(
            "note: Please set one in the .env file or set the $GITHUB_ACCESS_TOKEN environment variable")
        exit(1)
    else:
        return os.getenv("GITHUB_ACCESS_TOKEN")


def zulip_token():
    load_dotenv()
    # TODO: handle case when key not set
    return os.getenv("ZULIP_API_KEY")


def zulip_email():
    load_dotenv()
    # TODO: handle case when key not set
    return os.getenv("ZULIP_EMAIL_ID")
