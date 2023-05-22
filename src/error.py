class Error:
    def __init__(self, msg: str, exitout=True) -> None:
        self.red = '\033[91m'
        self.end = '\033[0m'
        self.orange = '\033[93m'
        self.exitout = exitout
        self.print_error(msg)

    def print_error(self, msg: str):
        if msg.lower().startswith("error"):
            if self.exitout:
                raise SystemExit(print(f"{self.red}{msg}{self.end}"))
            else:
                print(f"{self.red}{msg}{self.end}")
        elif msg.lower().startswithrtswith("warning") or msg.lower().startswith("note"):
            if self.exitout:
                raise SystemExit(print(f"{self.orange}{msg}{self.end}"))
            else:
                print(f"{self.orange}{msg}{self.end}")
        else:
            if self.exitout:
                print(f"error: {self.red}{msg}{self.end}")
            else: 
                print(f"error: {self.red}{msg}{self.end}")
