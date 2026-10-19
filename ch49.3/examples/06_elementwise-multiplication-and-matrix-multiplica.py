try:
    left @ np.ones((3, 1))
except ValueError:
    print("matrix inner dimensions do not match")

print("vector dot:", np.array([2, 1]) @ np.array([4, 5]))
