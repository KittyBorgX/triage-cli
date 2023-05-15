import sys


class CLIParser:
    def __init__(self):
        self.arg_len = len(sys.argv)
        self.args = sys.argv
        pass

    def has_arg(self, arg):
        res = False
        for i in self.args:
            if i == arg:
                res = True
                break
        return res

    def value_of_arg(self, arg):
        for i in self.args:
            if i == arg:
                if str(self.args[i+1]).rfind("-") or str(self.args[i+1]).rfind("--"):
                    print(
                        f"error: Argument {self.args[i+1]} must be an argument not a flag")
                    exit(1)
                return self.args[i+1]
        return None

    def help(self):
        print("triage-cli: A command line interface for triaging pull requests.")
        print()
        print("Usage: triage-cli [OPTIONS]")
        print()
        print("Options:")
        print("-pz, --post-to-zulip         Post the report on completion to zulip")
        print("-d, --details                Add additional details like createdTime to the report")
        print("-h, --help                   Print this help message")
