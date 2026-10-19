cells = {(0, 2): 8, (2, 0): 5}
for row in range(3):
    print([cells.get((row, column), 0) for column in range(4)])
print("stored entries:", len(cells))
print("missing cell stored:", (1, 1) in cells)
