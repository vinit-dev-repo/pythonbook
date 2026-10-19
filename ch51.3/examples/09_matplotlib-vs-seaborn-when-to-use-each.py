fig, ax = plt.subplots()
sns.boxplot(data=sales_df, x="city", y="price", ax=ax)   # seaborn draws the chart
ax.set_title("Styled with plain matplotlib")              # matplotlib finishes it
ax.axhline(15, color="red", linestyle="--", label="target price")
ax.legend()
plt.show()
