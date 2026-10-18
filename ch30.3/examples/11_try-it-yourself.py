from enum import Enum, IntFlag, auto, unique


# 1
class Toppings(IntFlag):
    CHEESE = auto()
    MUSHROOM = auto()
    OLIVES = auto()


pizza = Toppings.CHEESE | Toppings.OLIVES
print(Toppings.MUSHROOM in pizza)   # False
print(Toppings.CHEESE in pizza)     # True


# 2
class Level(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


def advice(level):
    match level:
        case Level.LOW:
            return "relax"
        case Level.MEDIUM:
            return "watch it"
        case Level.HIGH:
            return "act now"
        case _:
            raise ValueError("unhandled level")


print(advice(Level("high")))
try:
    advice(Level("extreme"))
except ValueError as error:
    print(error)


# 3
@unique
class Problem(Enum):
    EMPTY = (1, ValueError)
    MISSING = (2, KeyError)

    def __new__(cls, code, exception_type):
        member = object.__new__(cls)
        member._value_ = code
        member.exception_type = exception_type
        return member


print(Problem(2).exception_type.__name__)
try:
    @unique
    class Clash(Enum):
        FIRST = (1, ValueError)
        SECOND = (1, KeyError)

        def __new__(cls, code, exception_type):
            member = object.__new__(cls)
            member._value_ = code
            member.exception_type = exception_type
            return member
except ValueError as error:
    print(error)
