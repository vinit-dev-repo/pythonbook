scores = [55, 60, 62, 68, 70, 71, 72, 75, 78, 80, 82, 85, 88, 91, 95]

fig, ax = plt.subplots()
ax.hist(scores, bins=5, edgecolor="black")
ax.set_title("Score distribution")
ax.set_xlabel("Score")
ax.set_ylabel("Count")
plt.show()
