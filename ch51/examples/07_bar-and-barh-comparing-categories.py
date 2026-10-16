cities = ["London", "Tokyo", "Nairobi"]
avg_temps = [12.0, 23.6, 18.9]

fig, ax = plt.subplots()
bars = ax.bar(cities, avg_temps, color=["tab:blue", "tab:red", "tab:green"])
ax.bar_label(bars, fmt="%.1f")   # print the value above each bar
ax.set_title("Average temperature by city")
plt.show()
