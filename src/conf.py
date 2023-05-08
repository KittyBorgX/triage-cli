import os
from dotenv import load_dotenv

def backup(): 
    if os.getenv("TCLI_BACKUP_DIR") is None: return False
    else: return True
    
def backup_dir():
    load_dotenv()
    if os.getenv("TCLI_BACKUP_DIR") is not None:
        p = os.getenv("TCLI_BACKUP")
        if not os.path.exists(p):
            os.makedirs(p)
        return os.getenv("TCLI_BACKUP")
    else:
        return


def gh_token():
    load_dotenv()
    if os.getenv("GITHUB_ACCESS_TOKEN") is None:
        print("error: There is no github token set")
        print(
            "note: Please set one in the .env file or set the $GITHUB_ACCESS_TOKEN environment variable")
        exit(1)
    else:
        return os.getenv("GITHUB_ACCESS_TOKEN")
