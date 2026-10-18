import abc


class Task(abc.ABC):
    @abc.abstractmethod
    def label(self):
        return "task"


class IncompleteTask(Task):
    pass


class EmailTask(Task):
    def label(self):
        return f"email-{super().label()}"


class Factory(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def create(cls):
        return cls()


class Ticket(Factory):
    @classmethod
    def create(cls):
        return cls()


try:
    IncompleteTask()
except TypeError as error:
    print(type(error).__name__)
try:
    class BadFactory(abc.ABC):
        @abc.abstractmethod
        @classmethod
        def create(cls):
            return cls()
except AttributeError as error:
    print(type(error).__name__)
print(EmailTask().label())
print(type(Ticket.create()).__name__)
