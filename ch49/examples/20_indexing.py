grid = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print(grid[0, 0])   # first row, first column
print(grid[1, 2])   # second row, third column
print(grid[2, :])   # a whole row: row 2, every column
print(grid[:, 1])   # a whole column: every row, column 1
