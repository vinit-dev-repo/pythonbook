# 1
foods = ["pizza", "sushi", "tacos"]
print(foods[0])
print(foods[-1])

# 2
shopping = ["apple", "bread"]
shopping.append("milk")
shopping.insert(0, "tea")
print(shopping)         # ['tea', 'apple', 'bread', 'milk']
print(len(shopping))    # 4

# 3
grid = [[1, 2, 3], [4, 5, 6]]
print(grid[1][1])       # 5

# 4
numbers = [2, 4, 5, 6, 7]
kept = []
for n in numbers:
    if n % 2 != 0:
        kept.append(n)
print(kept)             # [5, 7]
