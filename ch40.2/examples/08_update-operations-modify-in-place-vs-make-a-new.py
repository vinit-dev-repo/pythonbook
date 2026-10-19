a = {1, 2, 3}
a |= {4, 5}          # a is modified in place
print(sorted(a))

b = {1, 2, 3}
new_b = b | {4, 5}    # b is untouched; new_b is a fresh set
print(sorted(b), sorted(new_b))
