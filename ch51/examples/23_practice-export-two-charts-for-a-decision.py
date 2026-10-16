from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

report = pd.DataFrame({
    "day": ["Mon", "Tue", "Wed"],
    "web": [8, 11, 9],
    "store": [13, 10, 15],
})
totals = report[["web", "store"]].sum()
assert totals.to_dict() == {"web": 28, "store": 38}
fig, axs = plt.subplots(1, 2, figsize=(8, 4))
bars = axs[0].bar(totals.index, totals.values)
axs[0].bar_label(bars)
axs[0].set_ylim(0, float(totals.max()) * 1.2)
axs[0].set_title("Total by channel")
axs[0].set_ylabel("Units sold")
for channel in ["web", "store"]:
    axs[1].plot(report["day"], report[channel], marker="o", label=channel)
axs[1].set_title("Sales by day")
axs[1].set_xlabel("Day")
axs[1].set_ylabel("Units sold")
axs[1].legend()
fig.suptitle("Three-day sales report")
fig.text(0.5, 0.02, "Illustrative three-day sample; no forecast", ha="center")
fig.tight_layout(rect=(0, 0.07, 1, 0.95))
destination = Path("channel-report.png")
fig.savefig(destination, dpi=150)
plt.close(fig)
assert destination.is_file() and destination.stat().st_size > 0
