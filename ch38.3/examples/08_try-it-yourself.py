import dis
import sys
import traceback

# 1
def scale(values, events):
    total = 0
    for value in values:
        try:
            total += value
        finally:
            events.append("cleaned")
    return total

names = {item.opname for item in dis.get_instructions(scale)}
print(bool(names & {"SETUP_LOOP", "SETUP_FINALLY"}), bool(scale.__code__.co_exceptiontable))
events = []
print(scale([1, 2], events), events)

# 2
def two_yields():
    yield "first"
    yield "second"

gen = two_yields()
first_line = two_yields.__code__.co_firstlineno
print(next(gen), gen.gi_frame.f_lineno - first_line)
print(next(gen), gen.gi_frame.f_lineno - first_line)

# 3
def inner():
    frame = sys._getframe()
    print(frame.f_code.co_name, frame.f_back.f_code.co_name)
    del frame

def outer():
    inner()

outer()

# 4
def divide(a, b):
    return a / b

def calculate(x):
    return divide(x, 0)

try:
    calculate(10)
except ZeroDivisionError as error:
    print([entry.name for entry in traceback.extract_tb(error.__traceback__)])
