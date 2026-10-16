numeric_df = sales_df[["units", "price"]]

fig, ax = plt.subplots()
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm",
            vmin=-1, vmax=1, center=0, ax=ax)
ax.set_title("Which columns move together?")
plt.show()
