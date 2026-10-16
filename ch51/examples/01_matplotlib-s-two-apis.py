import matplotlib.pyplot as plt

# the quick way (works, but hides what's really happening)
plt.plot([1, 2, 3], [10, 20, 15])
plt.title("Quick way")
plt.show()

# the object way (this chapter's habit)
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [10, 20, 15])
ax.set_title("Object way")
plt.show()
