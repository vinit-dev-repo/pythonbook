original = np.arange(6)
view = original.reshape(2, 3)
view[0, 0] = 999
safe = view.copy()
view[1, 2] = -5
safe[0, 1] = 88
print(original.tolist())
print(safe.tolist())
print(np.shares_memory(original, view), np.shares_memory(original, safe))
