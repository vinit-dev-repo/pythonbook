# class_factory_trace.py
from tracer_lab import Tracer, Counter

def trace_creation(name, bases, namespace):
    target_class = type(name, bases, namespace)
    return Tracer(target_class)

class TracedCounter(Counter, metaclass=trace_creation):
    pass

first, second = TracedCounter(5), TracedCounter(20)
print(first.add(2), second.add(3))
print(first._target.value, second._target.value)
print(isinstance(first, Counter), isinstance(first._target, Counter))
print(type(TracedCounter) is type)
