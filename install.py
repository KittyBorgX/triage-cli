#!/usr/bin/env python

import subprocess
import os

subprocess.run(["pip", "install", "-r", "requirements.txt"])
subprocess.run(["cp", "example.env", ".env"])

shell = os.getenv("SHELL")
wd = subprocess.getoutput("pwd")
curshell = subprocess.getoutput("ps -p $$ -oargs=")


if curshell.rfind("zsh"):
    # zsh shell, we modify $HOME/.zshrc
    zshrc = os.getenv("HOME") + "/.zshrc"
    with open(zshrc, 'a') as f:
        f.write(f"alias tcli=\"python {wd}/src/main.py\"")
    print()
    print()
    print("------------------------------------------------------------")
    print(
        f"Installation complete. Please run `source {zshrc}` to activate the `tcli` command in the current shell")
    print(
        f"Or reload the shell to load the triage-cli tool")
    print("------------------------------------------------------------")


elif curshell.rfind("bash"):
    # bash shell, we modify $HOME/.bashrc
    bashrc = os.getenv("HOME") + "/.bashrc"
    with open(bashrc, 'a') as f:
        f.write(f"alias tcli={wd}/src/main.py")
    print("------------------------------------------------------------")
    print(
        f"Installation complete. Please run `source {bashrc}` to activate the `tcli` command in the current shell")
    print(
        f"Or reload the shell to load the triage-cli tool")
    print("------------------------------------------------------------")
