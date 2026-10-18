from enum import Enum, auto

class CodePool(Enum):
    def _generate_next_value_(name, start, count, last_values):
        print(name, count, last_values)
        for candidate in (10, 20, 40):
            if candidate not in last_values:
                return candidate
        raise ValueError('code pool exhausted')

class Channel(CodePool):
    MAIL = 10
    POST = 10
    SMS = auto()
    PUSH = auto()

print([(item.name, item.value) for item in Channel])
print(Channel.POST is Channel.MAIL)
try:
    class Full(CodePool):
        A = 10
        B = 20
        C = 40
        D = auto()
except ValueError as error:
    print(error)
