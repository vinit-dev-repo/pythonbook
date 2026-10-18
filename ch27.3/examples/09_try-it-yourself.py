import functools


# 1
def add_hello(cls):
    def hello(self):
        return "hello from " + type(self).__name__

    cls.hello = hello
    return cls


@add_hello
class Robot:
    pass


print(Robot().hello())


# 2
class Drone:
    pass


Drone = add_hello(Drone)
print(Drone().hello())


def forgetful(cls):
    cls.hello = lambda self: "hi"


@forgetful
class Lost:
    pass


print(Lost)


# 3
@functools.total_ordering
class Ticket:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return self.number == other.number

    def __lt__(self, other):
        return self.number < other.number


print(Ticket(1) <= Ticket(2), Ticket(3) >= Ticket(2))
