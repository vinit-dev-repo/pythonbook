# 1
nums = [1, 2, 3, 4, 5]
print({n: (n % 2 == 0) for n in nums})      # {1: False, 2: True, 3: False, 4: True, 5: False}

# 2
letters = ["a", "b", "a", "c", "b"]
print(sorted({letter.upper() for letter in letters}))   # ['A', 'B', 'C']
# (a plain print(...) here would show the same three letters, but sets
#  don't promise an order, so the arrangement printed can vary between runs)

# 3
keys = ["a", "b", "c"]
values = [1, 2, 3]
print({k: v for k, v in zip(keys, values)})     # {'a': 1, 'b': 2, 'c': 3}

# 4
data = [1, 2, 3]
tripled = [last := n * 3 for n in data]
print(tripled)                                  # [3, 6, 9]
print(last)                                     # 9
