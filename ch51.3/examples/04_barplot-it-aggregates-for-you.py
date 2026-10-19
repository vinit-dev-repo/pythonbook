fig, ax = plt.subplots()
sns.barplot(data=sales_df, x="city", y="price", seed=7, ax=ax)
ax.set_title("Average price by city (auto-aggregated)")
plt.show()
