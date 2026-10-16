sales_df = pd.DataFrame({
    "units": [5, 2, 1, 8, 3, 4, 6],
    "price": [9.99, 19.99, 19.99, 9.99, 9.99, 19.99, 9.99],
    "city": ["London", "Tokyo", "London", "Nairobi", "Tokyo", "Nairobi", "London"],
})

fig, ax = plt.subplots()
sns.scatterplot(data=sales_df, x="units", y="price", hue="city", s=100, ax=ax)
ax.set_title("Orders coloured by city")
plt.show()
