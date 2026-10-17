# 1
nums = [3, 8, 15, 20, 4, 11]
print([n for n in nums if n > 10])          # [15, 20, 11]

# 2
words = ["hi", "hello", "hey", "greetings"]
print([w.upper() for w in words])           # ['HI', 'HELLO', 'HEY', 'GREETINGS']

# 3
readings = [[1, 2], [3, 4]]
print([value * 2 for row in readings for value in row])     # [2, 4, 6, 8]
