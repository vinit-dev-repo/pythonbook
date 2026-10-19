fig, ax = plt.subplots()
ax.scatter(london, nairobi, s=80, c="tab:purple")   # s=size, c=colour
ax.set_xlabel("London temp")
ax.set_ylabel("Nairobi temp")
ax.set_title("Do the two cities move together?")
plt.show()
