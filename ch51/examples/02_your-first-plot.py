import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temps = [12, 14, 11, 9, 10, 13, 15]

fig, ax = plt.subplots()
ax.plot(days, temps)
ax.set_title("A week of temperatures")
ax.set_xlabel("Day")
ax.set_ylabel("Degrees C")
plt.show()
