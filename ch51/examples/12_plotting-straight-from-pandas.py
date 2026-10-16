import pandas as pd

df = pd.DataFrame({"city": cities, "avg_temp": avg_temps})
ax = df.plot(x="city", y="avg_temp", kind="bar", title="Average temp",
             legend=False, rot=0)
ax.figure.tight_layout()
plt.show()
