# 1
foods = ["pizza", "sushi", "tacos"]
print(foods[0])
print(foods[-1])

# 2
numbers = [4, 8, 15, 16, 23, 42]
print(numbers[1:5])   # [8, 15, 16, 23]

# 3
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)   # [1, 2, 3]
print(b)   # [1, 2, 3, 4]

# 4
full_name = "Ada Lovelace"
first, last = full_name.split()
print(first)   # Ada
print(last)    # Lovelace

# 5
price = 19.999
print(f"${price:.2f}")   # $20.00

# 6
print(ord("Z"))          # 90
print(chr(9731))         # ☃
