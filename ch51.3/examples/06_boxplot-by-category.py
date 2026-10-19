fig, ax = plt.subplots()
sns.boxplot(data=sales_df, x="city", y="price", ax=ax)
ax.set_title("Price spread by city")
plt.show()
