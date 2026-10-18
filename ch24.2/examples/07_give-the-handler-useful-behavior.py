class FormatFailure(Exception):
    def __init__(self, filename, line):
        self.filename = filename
        self.line = line
        super().__init__(f"Invalid data in {filename} at line {line}")

    def details(self):
        return f"{self.filename}:{self.line}"

class HeaderFailure(FormatFailure):
    def details(self):
        return f"header {super().details()}"

def read_record(problem):
    raise problem

for problem in (FormatFailure("a.txt", 2), HeaderFailure("b.txt", 1)):
    try:
        read_record(problem)
    except FormatFailure as error:
        print(error.details())
