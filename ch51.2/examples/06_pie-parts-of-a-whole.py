channels = ["Web", "Mobile", "Store"]
orders = [45, 30, 25]
fig, ax = plt.subplots()
ax.pie(orders, labels=channels, autopct="%1.0f%%")
ax.set_title("Share of orders by channel")
plt.show()
