readings = np.array([[7, 9, 8, 12], [15, 13, 16, 14]])
before = readings.copy()
print(readings.mean(axis=1).tolist())
print(readings.max(axis=0).tolist())
print(int((readings < 10).sum()))
try:
    readings.reshape(3, 3)
except ValueError:
    print("8 values cannot fill 9 positions")
print(readings.reshape(4, 2).shape)
assert np.array_equal(readings, before)
