# 1
def square(x):
    return x * x

import dis
dis.dis(square)
# RESUME, LOAD_FAST 0 (x), LOAD_FAST 0 (x), BINARY_OP (*), RETURN_VALUE
# Conceptual loads: Python 3.15 may fuse them into one instruction.

# 2
def demo():
    for i in range(3):
        try:
            pass
        finally:
            pass

dis.dis(demo)
# Empty try/finally may be optimised away, so its table can be empty.
# SETUP_LOOP / SETUP_FINALLY are absent on this interpreter.

# 3
GLOBAL_RATE = 0.1

def uses_only_locals(price, rate):
    return price * rate

def uses_a_global(price):
    return price * GLOBAL_RATE

dis.dis(uses_only_locals)   # LOAD_FAST for both price and rate
dis.dis(uses_a_global)      # LOAD_FAST for price, LOAD_GLOBAL for GLOBAL_RATE

# 4
# import mymodule                                  # __pycache__/mymodule.cpython-315.pyc appears
# (edit mymodule.py, add a print() to it)
# import importlib; importlib.reload(mymodule)     # or simply run your script again
# compare the cached bytes before and after changing the source code

# 5
def two_yields():
    yield "first"
    yield "second"

gen = two_yields()
print(next(gen))
print(gen.gi_frame.f_lineno)
print(next(gen))
print(gen.gi_frame.f_lineno)
