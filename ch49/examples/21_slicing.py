grid = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print(grid[0:2, :])      # top 2 rows, all columns
print(grid[:, 1:3])      # all rows, columns 1 and 2
print(grid[0:2, 1:3])    # the top-right 2x2 block
