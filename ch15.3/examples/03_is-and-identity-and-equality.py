a = [1, 2, 3]
b = [1, 2, 3]        # a separate, equal-looking list
c = a                # the SAME list as a

print(a == b)         # equal contents?  Yes
print(a is b)         # the same object?  No — two different lists
print(a is c)         # the same object?  Yes
