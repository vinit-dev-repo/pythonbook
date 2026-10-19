# axis_selection.py
import numpy as np

batch = np.arange(24).reshape(2, 3, 4)
measurement = batch[..., 1]
expanded = batch[:, None, ...]
print(measurement.tolist())
print(expanded.shape)
print(np.shares_memory(batch, measurement))
print(np.shares_memory(batch, expanded))
