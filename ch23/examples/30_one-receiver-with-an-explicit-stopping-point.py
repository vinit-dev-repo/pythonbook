class TerminalDevice:
    def setup(self):
        print("terminal")

class ContinuingScanner(TerminalDevice):
    def setup(self):
        print("scanner")
        super().setup()

class StoppingPrinter(TerminalDevice):
    def setup(self):
        print("printer stops")

class StoppedAllInOne(StoppingPrinter, ContinuingScanner):
    def setup(self):
        print("combined")
        super().setup()

StoppedAllInOne().setup()
