import dis

def minutes_in_a_day():
    return 24 * 60

print(minutes_in_a_day())
print("co_consts:", minutes_in_a_day.__code__.co_consts)
dis.dis(minutes_in_a_day)
