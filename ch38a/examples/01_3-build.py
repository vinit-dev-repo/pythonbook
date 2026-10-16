import dis

def minutes_per_day():
    return 24 * 60

print(minutes_per_day())
print(1440 in minutes_per_day.__code__.co_consts)
print(any(i.opname == "BINARY_OP" for i in dis.get_instructions(minutes_per_day)))
