original = np.arange(6)
view = original.reshape(2, 3)
view[0, 0] = 999
print(original)
