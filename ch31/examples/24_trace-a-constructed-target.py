from tracer_lab import Tracer, Counter

WrappedCounter = Tracer(Counter)
left = WrappedCounter(2)
right = WrappedCounter(8)
print(left.value)
left.lookups = 99
print(right.add(1))
print(left.lookups, right.lookups)
print(left._target.value, right._target.value)
