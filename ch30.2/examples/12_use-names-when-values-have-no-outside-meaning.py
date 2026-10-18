from enum import Enum, auto

class PreviousValue(Enum):
    def _generate_next_value_(name, start, count, last_values):
        if not last_values:
            raise ValueError('an alias needs a previous value')
        return last_values[-1]

class WindowState(PreviousValue):
    OPEN = object()
    OPENED = auto()
    CLOSED = object()
    SHUT = auto()

print([item.name for item in WindowState])
print(WindowState.OPENED is WindowState.OPEN)
print(WindowState['SHUT'] is WindowState.CLOSED)
print(WindowState(WindowState.OPEN.value) is WindowState.OPEN)
try:
    WindowState(object())
except ValueError as error:
    print(type(error).__name__)
try:
    class MissingFirst(PreviousValue):
        ALIAS = auto()
except ValueError as error:
    print(error)
