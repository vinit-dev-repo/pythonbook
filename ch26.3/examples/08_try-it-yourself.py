import abc
import collections.abc


# 1
class ThirdPartyQueue:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop(0)


class Queue(abc.ABC):
    @abc.abstractmethod
    def push(self, item):
        pass

    @abc.abstractmethod
    def pop(self):
        pass

    def describe(self):
        return "a queue"


Queue.register(ThirdPartyQueue)
print(isinstance(ThirdPartyQueue(), Queue))


# 2
print(Queue in ThirdPartyQueue.__mro__)
try:
    ThirdPartyQueue().describe()
except AttributeError:
    print("no describe: nothing was inherited")


# 3
class Meter:
    def __len__(self):
        return 3


class Plain:
    pass


print(isinstance(Meter(), collections.abc.Sized))
print(isinstance(Plain(), collections.abc.Sized))
