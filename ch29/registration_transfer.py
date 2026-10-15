# registration_transfer.py
from types import MethodType


def greet(self):
    return f"hello, {self.name}"


class Member:
    say = greet                 # class storage: descriptor binding works

    def __init__(self, name):
        self.name = name
        self._registered = None

    def register(self, function):
        self._registered = MethodType(function, self)

    def perform(self):
        if self._registered is None:
            raise RuntimeError("no behavior registered")
        return self._registered()


def sign_in(self):
    self.visits += 1
    return f'{self.name} signed in: {self.visits}'


if __name__ == '__main__':
    ada = Member('Ada')
    lin = Member('Lin')
    try:
        ada.perform()
    except RuntimeError as error:
        print(type(error).__name__)

    ada.register(sign_in)
    lin.register(sign_in)
    try:
        ada.perform()
    except AttributeError as error:
        print(type(error).__name__, hasattr(ada, 'visits'))

    assert not hasattr(ada, 'visits')
    assert ada.name == 'Ada'
    ada.visits = 0
    lin.visits = 0
    saved = ada._registered
    assert saved.__func__ is sign_in
    assert (ada.visits, lin.visits) == (0, 0)
    print(saved.__self__ is ada, ada.visits, lin.visits)
    print(ada.perform())
    print(lin.perform())
    assert (ada.visits, lin.visits) == (1, 1)
    lin._registered = saved
    print(lin.perform())
    print(ada.visits, lin.visits, saved.__self__ is ada)
    assert (ada.visits, lin.visits) == (2, 1)
    assert lin._registered.__self__ is ada
