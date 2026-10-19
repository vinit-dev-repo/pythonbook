import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1
df = pd.DataFrame({
    "value": [10, 12, 9, 40, 42, 39, 20, 22, 19],
    "group": ["A", "A", "A", "B", "B", "B", "C", "C", "C"],
})
fig, ax = plt.subplots()
sns.boxplot(data=df, x="group", y="value", ax=ax)
plt.show()
