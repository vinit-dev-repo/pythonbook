# counted.py
from functools import update_wrapper

class BoundCall:
    def __init__(self, decorator, subject):
        update_wrapper(self, decorator.func, updated=())
        self.decorator = decorator
        self.subject = subject

    def __call__(self, *args, **kwargs):
        return self.decorator._call_subject(self.subject, *args, **kwargs)


class UnboundCall:
    def __init__(self, decorator):
        self.decorator = decorator

    def __call__(self, subject, /, *args, **kwargs):
        return self.decorator._call_subject(subject, *args, **kwargs)


class CountedCalls:
    def __init__(self, func):
        update_wrapper(self, func, updated=())
        self.func = func
        self.total_calls = 0

    def __get__(self, subject, owner=None):
        if subject is None:
            return UnboundCall(self)
        return BoundCall(self, subject)

    def _call_subject(self, subject, *args, **kwargs):
        subject._call_counts[self] = subject._call_counts.get(self, 0) + 1
        self.total_calls += 1
        return self.func(subject, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        self.total_calls += 1
        return self.func(*args, **kwargs)

    def calls_for(self, subject):
        return subject._call_counts.get(self, 0)


class ClosureCountedCalls(CountedCalls):
    def __get__(self, subject, owner=None):
        if subject is None:
            return UnboundCall(self)

        def call(*args, **kwargs):
            return self._call_subject(subject, *args, **kwargs)

        update_wrapper(call, self.func, updated=())
        call.decorator = self
        call.subject = subject
        return call


def counted(func):
    return CountedCalls(func)
