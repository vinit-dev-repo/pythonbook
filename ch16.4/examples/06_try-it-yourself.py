# 1
scores = [True, True, False, True, False]
print(sum(scores))       # 3

# 2
for value in (0, 1, "", "hi", [], [1], None):
    print(repr(value), bool(value))
# 0 False, 1 True, '' False, 'hi' True, [] False, [1] True, None False

# 3
nickname = ""
print(nickname or "Anonymous")                      # Anonymous
quantity = 0
print(quantity or 10)                               # 10  (wrong: 0 was valid)
print(10 if quantity is None else quantity)         # 0
