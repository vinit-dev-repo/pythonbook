# 1
a = [1, 2]
b = a
b.append(3)
print(a, b, a is b)
# 2
a = [1, 2]
b = a.copy()
b.append(3)
print(a, b, a is b)
# 3
def double_it(n):
    n = n * 2
    return n
value = 5
print(double_it(value), value)
value = double_it(value)
print(value)
