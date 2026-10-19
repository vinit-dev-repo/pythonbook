def add_ge_from_lt(cls):
    if "__eq__" not in cls.__dict__ or "__lt__" not in cls.__dict__:
        raise TypeError("define __eq__ and __lt__ in this class first")
    if "__ge__" not in cls.__dict__:
        cls.__ge__ = ge_from_lt
    return cls


def ge_from_lt(self, other):
    result = self.__lt__(other)
    if result is NotImplemented:
        return NotImplemented
    return not result


class Ticket:
    def __init__(self, score):
        self.score = score

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.score == other.score
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self.score < other.score
        return NotImplemented


print("__ge__" in Ticket.__dict__)
Ticket = add_ge_from_lt(Ticket)
print("__ge__" in Ticket.__dict__)
print(Ticket(8) >= Ticket(5))
try:
    Ticket(8) >= 5
except TypeError as error:
    print(type(error).__name__)


class ExistingTicket:
    def __eq__(self, other):
        return NotImplemented

    def __lt__(self, other):
        return NotImplemented

    def __ge__(self, other):
        return "kept"


saved_ge = ExistingTicket.__ge__
ExistingTicket = add_ge_from_lt(ExistingTicket)
print(ExistingTicket.__ge__ is saved_ge)
print(ExistingTicket() >= ExistingTicket())
