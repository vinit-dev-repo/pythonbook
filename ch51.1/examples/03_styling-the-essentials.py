fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(days, temps, color="tab:blue", linestyle="--", marker="o",
        linewidth=2, label="London")
ax.set_title("Styled line")
ax.legend()
ax.grid(True)
plt.show()
