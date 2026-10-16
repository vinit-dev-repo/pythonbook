from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    HIGH = 3

class ExitCode(IntEnum):
    RETRY = 1

result = Priority.HIGH + 1
print(result, type(result).__name__)
print(Priority.LOW == ExitCode.RETRY)
print(len({Priority.LOW, ExitCode.RETRY, 1}))
