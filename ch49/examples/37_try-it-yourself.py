import numpy as np

# 1
grid = np.arange(1, 21).reshape(4, 5)
print(grid)

# 2
print(grid[:, 1:3])

# 3
print(grid[grid > 10])

# 4
a = np.array([1, 2, 3])
b = np.array([[10], [20], [30]])
print(a + b)   # broadcasts to shape (3, 3)

# 5
scores = np.array([[5, 8, 9], [7, 6, 10]])
print(scores.mean(axis=1))   # per row -> collapse columns
print(scores.max(axis=0))    # per column -> collapse rows
