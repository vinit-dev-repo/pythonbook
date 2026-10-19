source = """
def outer():
    x = 1
    def inner():
        return x + 1
    return inner
"""
ns = {}
exec(compile(source, "<example>", "exec"), ns)
outer = ns["outer"]

outer_code = outer.__code__
import re
def mask(obj):
    """Same address-masking trick as the previous section, so this stays reproducible."""
    return re.sub(r"0x[0-9A-Fa-f]+", "0x...", repr(obj))

print("outer co_consts:", mask(outer_code.co_consts))
print("outer co_varnames:", outer_code.co_varnames)
print("outer co_cellvars:", outer_code.co_cellvars)

inner_code = [c for c in outer_code.co_consts if hasattr(c, "co_name")][0]
print("inner code object:", mask(inner_code))
print("inner co_freevars:", inner_code.co_freevars)
print("inner co_names:", inner_code.co_names)
