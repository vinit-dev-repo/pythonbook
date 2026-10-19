import matplotlib.pyplot as plt

# 2
days = ["Mon", "Tue", "Wed"]
fig, ax = plt.subplots()
ax.plot(days, [3, 5, 4], label="first", linestyle="--", marker="o")
ax.plot(days, [2, 3, 6], label="second", marker="s")
ax.legend()
print(len(ax.lines))
print(ax.get_legend_handles_labels()[1])
plt.close(fig)

# 3
fig, axs = plt.subplots(2, 1, sharex=True)
print(axs.shape)
axs[0].plot(days, [3, 5, 4])
axs[0].set_title("Line")
axs[1].bar(days, [2, 3, 6])
axs[1].set_title("Bars")
print([ax.get_title() for ax in axs])
plt.close(fig)
