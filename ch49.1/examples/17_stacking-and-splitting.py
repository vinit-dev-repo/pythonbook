a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.vstack([a, b]))         # stack as new ROWS ("v" = vertical)
print(np.hstack([a, b]))         # stack side by side ("h" = horizontal)
print(np.concatenate([a, b]))    # the general-purpose version
