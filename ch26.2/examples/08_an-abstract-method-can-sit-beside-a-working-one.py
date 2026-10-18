import abc

try:
    class BadFactory(abc.ABC):
        @abc.abstractmethod
        @classmethod
        def create(cls):
            return cls()
except AttributeError as error:
    print(type(error).__name__)

class Factory(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def create(cls):
        return cls()

class Ticket(Factory):
    @classmethod
    def create(cls):
        return cls()

print(type(Ticket.create()).__name__)
