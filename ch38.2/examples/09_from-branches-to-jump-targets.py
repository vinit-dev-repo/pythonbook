import dis

def sum_nonnegative(values):
    total = 0
    for value in values:
        if value < 0:
            continue
        total += value
    return total

instructions = list(dis.get_instructions(sum_nonnegative))
targets = {instruction.offset: instruction.opname
           for instruction in instructions}
print("result:", sum_nonnegative([-2, 4, 0, 3]))
for instruction in instructions:
    if instruction.jump_target is not None:
        direction = ("backward" if instruction.jump_target < instruction.offset
                     else "forward")
        print(instruction.opname, direction, targets[instruction.jump_target])
