import numpy as np

fig, axs = plt.subplots(2, 2, figsize=(8, 6))

axs[0, 0].plot(days, london, color="tab:blue")
axs[0, 0].set_title("London line")
axs[0, 0].set_ylabel("Degrees C")

axs[0, 1].bar(days, nairobi, color="tab:orange")
axs[0, 1].set_title("Nairobi bar")
axs[0, 1].set_ylabel("Degrees C")

axs[1, 0].hist(np.random.default_rng(1).normal(20, 3, 200), bins=15)
axs[1, 0].set_title("Random distribution")
axs[1, 0].set_xlabel("Simulated value")
axs[1, 0].set_ylabel("Count")

axs[1, 1].scatter(london, nairobi)
axs[1, 1].set_title("London vs Nairobi")
axs[1, 1].set_xlabel("London degrees C")
axs[1, 1].set_ylabel("Nairobi degrees C")

fig.tight_layout()
plt.show()
