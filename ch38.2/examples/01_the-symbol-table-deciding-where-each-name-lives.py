import symtable

source = """
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
"""

def child_named(table, name):
    """Find a nested block by NAME.

    Do not index get_children() by position. What sits at index 0 is not part of the
    language's promise, and it changed in 3.14: deferred annotations (PEP 649) add an
    `__annotate__` block, which now comes first at module level.
    """
    for child in table.get_children():
        if child.get_name() == name:
            return child
    raise LookupError(name)

top = symtable.symtable(source, "<string>", "exec")
make_counter = child_named(top, "make_counter")
counter = child_named(make_counter, "counter")

print("module symbols:", sorted(top.get_identifiers()))
print()
print("make_counter symbols:", sorted(make_counter.get_identifiers()))
for name in sorted(make_counter.get_identifiers()):
    sym = make_counter.lookup(name)
    print(f"  {name}: local={sym.is_local()} free={sym.is_free()} global={sym.is_global()}")
print()
print("counter symbols:", sorted(counter.get_identifiers()))
for name in sorted(counter.get_identifiers()):
    sym = counter.lookup(name)
    print(f"  {name}: local={sym.is_local()} free={sym.is_free()} global={sym.is_global()}")
