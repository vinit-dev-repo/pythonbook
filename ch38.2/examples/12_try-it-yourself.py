import dis

# 1
def square(x):
    return x * x

print([item.opname for item in dis.get_instructions(square)])

# 2
GLOBAL_RATE = 0.1

def uses_only_locals(price, rate):
    return price * rate

def uses_a_global(price):
    return price * GLOBAL_RATE

for function in (uses_only_locals, uses_a_global):
    names = {item.opname for item in dis.get_instructions(function)}
    print(function.__name__, any(n.startswith("LOAD_FAST") for n in names), "LOAD_GLOBAL" in names)

# 3
def add_tax(price, rate=0.1):
    total = price + price * rate
    return total

code = add_tax.__code__
print(code.co_varnames, code.co_argcount, code.co_names)

# 4
def make_counter():
    count = 0
    def counter():
        return count
    return counter

inner = next(c for c in make_counter.__code__.co_consts if hasattr(c, "co_name"))
print(make_counter.__code__.co_cellvars, inner.co_freevars)
