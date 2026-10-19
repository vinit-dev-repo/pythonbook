a = Counter(apple=3, banana=2)
b = Counter(apple=1, banana=4, cherry=1)

print(a + b)    # add counts together
print(a - b)    # subtract; results at or below 0 are dropped
print(a & b)    # minimum of each shared key
print(a | b)    # maximum of each key
