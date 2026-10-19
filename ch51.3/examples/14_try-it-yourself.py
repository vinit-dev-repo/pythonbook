import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 2
frame = pd.DataFrame({"group": ["A", "A", "B", "B"], "value": [1, 3, 5, 7], "other": [2, 4, 6, 8]})
fig, ax = plt.subplots()
sns.barplot(data=frame, x="group", y="value", ax=ax)
print([round(float(bar.get_height()), 1) for bar in ax.patches])
plt.close(fig)

# 3
grid = sns.pairplot(frame)
print(type(grid).__name__)
fig, ax = plt.subplots()
returned = sns.boxplot(data=frame, x="group", y="value", ax=ax)
print(returned is ax)
plt.close(fig)
plt.close(grid.figure)
