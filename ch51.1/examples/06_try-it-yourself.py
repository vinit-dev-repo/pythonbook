import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1
fig, ax = plt.subplots()
ax.plot(["A", "B", "C", "D", "E"], [3, 7, 2, 9, 4])
ax.set_title("Exercise 1")
plt.show()
