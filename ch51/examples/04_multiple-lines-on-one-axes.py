london = [12, 14, 11, 9, 10, 13, 15]
nairobi = [22, 24, 23, 25, 26, 24, 21]

fig, ax = plt.subplots()
ax.plot(days, london, label="London", marker="o")
ax.plot(days, nairobi, label="Nairobi", marker="s")
ax.set_title("Two cities")
ax.legend()
plt.show()
