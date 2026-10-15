# selected_updates.py
import numpy as np

levels = np.array([3, 6, 9, 12])
selected = levels[[0, 2]]
selected[:] = -1
print(levels.tolist())
levels[[0, 2]] = [30, 90]
print(levels.tolist())
print(selected.tolist())
