class UnclearFailure(Exception):
    def __init__(self, filename, line):
        self.filename = filename
        self.line = line

positional = UnclearFailure("a.txt", 2)
keyword = UnclearFailure(filename="a.txt", line=2)
print(positional.args, repr(str(positional)))
print(keyword.args, repr(str(keyword)))
