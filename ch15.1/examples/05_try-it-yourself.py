# 1
x = 10
print(type(x))     # <class 'int'>
x = "ten"
print(type(x))     # <class 'str'>

# 2
x = [1, 2, 3]
before = id(x)
x = [4, 5, 6]
print(id(x) == before)   # False

# 3
x = []
original = x
x = x
print(x is original)     # True
