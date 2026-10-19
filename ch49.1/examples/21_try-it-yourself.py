import numpy as np

# 2
steps = np.arange(0, 1, 0.25)
points = np.linspace(0, 1, 5)
print(steps.tolist())
print(points.tolist())
print(len(steps), len(points))

# 3
original = np.arange(6)
view = original.reshape(2, 3)
view[0, 0] = 100
print(original.tolist())
safe = original.reshape(2, 3).copy()
safe[1, 2] = -1
print(original.tolist())
print(np.shares_memory(original, view), np.shares_memory(original, safe))
