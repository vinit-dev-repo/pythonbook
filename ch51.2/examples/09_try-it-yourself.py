import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1
fig, ax = plt.subplots()
bars = ax.bar(["Widget", "Gadget", "Gizmo"], [120, 90, 150])
ax.bar_label(bars)
plt.show()

# 2
data = np.random.default_rng(0).normal(50, 10, 200)
fig, ax = plt.subplots()
ax.hist(data, bins=15)
plt.show()

# 3
fig, axs = plt.subplots(1, 2, figsize=(8, 4))
axs[0].plot([1, 2, 3], [10, 20, 15])
axs[1].hist(data, bins=15)
fig.tight_layout()
plt.show()
