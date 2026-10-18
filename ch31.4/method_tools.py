# method_tools.py
from functools import wraps
from types import FunctionType

def counted(func):
    @wraps(func)
    def call(*args, **kwargs):
        call.calls += 1
        return func(*args, **kwargs)
    call.calls = 0
    return call

def method_metaclass(decorate):
    class MethodMeta(type):
        def __new__(mcs, name, bases, namespace, **kwargs):
            updated = dict(namespace)
            for key, value in namespace.items():
                if type(value) is FunctionType:
                    updated[key] = decorate(value)
            return super().__new__(mcs, name, bases, updated, **kwargs)
    return MethodMeta

def decorate_methods(decorate):
    def apply(cls):
        for key, value in list(vars(cls).items()):
            if type(value) is FunctionType:
                setattr(cls, key, decorate(value))
        return cls
    return apply

class Base:
    def report(self):
        return "base"

def make_bucket(meta=type, decorate=lambda cls: cls):
    @decorate
    class Bucket(Base, metaclass=meta):
        def __init__(self):
            self.amount = 0

        def add(self, amount):
            if amount < 0:
                raise ValueError("negative amount")
            self.amount += amount
            return self.amount

        def report(self):
            return super().report(), self.amount

        @classmethod
        def kind(cls):
            return cls.__name__

        @property
        def empty(self):
            return self.amount == 0
    return Bucket

if __name__ == "__main__":
    CounterMeta = method_metaclass(counted)
    MetaBucket = make_bucket(meta=CounterMeta)
    DecoratedBucket = make_bucket(decorate=decorate_methods(counted))
    for label, cls in [("meta", MetaBucket), ("decorator", DecoratedBucket)]:
        first, second = cls(), cls()
        print(label, first.add(3), second.report(), first.empty)
        try:
            first.add(-1)
        except ValueError:
            print("rejected", first.amount)
        print(cls.__init__.calls, cls.add.calls, cls.report.calls)
        print(type(first) is cls, hasattr(cls.kind, "calls"))
