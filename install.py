import subprocess
import os

subprocess.run(["pip", "install", "-r", "requirements.txt"])
subprocess.run(["cp", "example.env", ".env"])

shell = os.getenv("SHELL")
wd = subprocess.getoutput("pwd")


if shell.rfind("bash"):
    # bash shell, we modify $HOME/.bashrc
    bashrc = os.getenv("HOME") + "/.bashrc"
    with open(bashrc, 'a') as f:
        f.write(f"alias tcli={wd}/src/main.py")
    subprocess.run(["source", f"{bashrc}"])


elif shell.rfind("zsh"):
    # bash shell, we modify $HOME/.bashrc
    zshrc = os.getenv("HOME") + "/.zshrc"
    with open(zshrc, 'a') as f:
        f.write(f"alias tcli={wd}/src/main.py")
    subprocess.run(f"source {zshrc}")
