import numpy as np

grid = np.arange(1, 21).reshape(4, 5)

# 1
print(grid[:, 1:3])

# 2
print(grid[grid > 10])
