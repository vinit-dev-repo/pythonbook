import numpy as np
sample = np.array([2, 4, 6])
print(round(float(sample.std()), 3))
print(float(sample.std(ddof=1)))
