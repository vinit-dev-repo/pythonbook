numbers = [1, 2, 3, 4, 5, 6]

# A map/filter chain places the filtering expression inside the mapping expression
result = list(map(lambda n: n * n, filter(lambda n: n % 2 == 0, numbers)))
print(result)

# comprehension — reads left to right
result = [n * n for n in numbers if n % 2 == 0]
print(result)
