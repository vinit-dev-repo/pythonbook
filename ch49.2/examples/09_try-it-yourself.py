import numpy as np

# 3
temps = np.array([18, 25, 31, 15, 40, 22])
temps[temps > 30] = 30
print(temps.tolist())
mild = (temps > 15) & (temps < 30)
print(temps[mild].tolist())
print(np.where(temps < 20, 0, temps).tolist())
