import dis

def small_repeat():
    return (1, 2) * 3

def big_repeat():
    return (1, 2) * 10000

print(small_repeat.__code__.co_consts)
print(big_repeat.__code__.co_consts)
