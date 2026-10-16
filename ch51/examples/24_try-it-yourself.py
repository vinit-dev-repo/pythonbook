import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1
fig, ax = plt.subplots()
ax.plot(["A", "B", "C", "D", "E"], [3, 7, 2, 9, 4])
ax.set_title("Exercise 1")
plt.show()

# 2
fig, ax = plt.subplots()
bars = ax.bar(["Widget", "Gadget", "Gizmo"], [120, 90, 150])
ax.bar_label(bars)
plt.show()

# 3
data = np.random.default_rng(0).normal(50, 10, 200)
fig, ax = plt.subplots()
ax.hist(data, bins=15)
plt.show()

# 4
df = pd.DataFrame({
    "value": [10, 12, 9, 40, 42, 39, 20, 22, 19],
    "group": ["A", "A", "A", "B", "B", "B", "C", "C", "C"],
})
fig, ax = plt.subplots()
sns.boxplot(data=df, x="group", y="value", ax=ax)
plt.show()

# 5
fig, axs = plt.subplots(1, 2, figsize=(8, 4))
axs[0].plot([1, 2, 3], [10, 20, 15])
axs[1].hist(data, bins=15)
fig.tight_layout()
plt.show()
