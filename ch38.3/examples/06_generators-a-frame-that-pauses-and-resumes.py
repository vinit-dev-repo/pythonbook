import dis

def running_totals(readings):
    total = 0
    for reading in readings:
        total += reading
        replacement = yield total
        if replacement is not None:
            total = replacement
    return total

print("generator flag:", bool(running_totals.__code__.co_flags & 0x20))
selected = {"RETURN_GENERATOR", "RESUME", "YIELD_VALUE", "RETURN_VALUE"}
for instruction in dis.get_instructions(running_totals):
    if instruction.opname in selected:
        print(instruction.opname)
