source = """
def add_tax(price, rate=0.1):
    total = price + price * rate
    return total
"""
ns = {}
exec(compile(source, "<example>", "exec"), ns)
add_tax = ns["add_tax"]

code = add_tax.__code__
# repr(code) embeds a real memory address that is different on every run (same idea as
# id() in [[15.1 - Names, Types and Rebinding]]); it is masked to "0x..." here so this listing
# stays exactly reproducible. Run print(code) yourself to see the real, varying address.
import re
print(re.sub(r"0x[0-9A-Fa-f]+", "0x...", repr(code)))
print("co_varnames:", code.co_varnames)
print("co_consts:", code.co_consts)
print("co_names:", code.co_names)
print("co_argcount:", code.co_argcount)
print("co_flags:", code.co_flags)
