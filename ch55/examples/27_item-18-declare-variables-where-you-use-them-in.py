# C-style — squares is declared before it's needed and stays alive long after
squares = []
for n in range(5):
    squares.append(n * n)
print(squares)

# Pythonic — squares is created exactly where it's needed, nothing to leak
squares = [n * n for n in range(5)]
print(squares)
