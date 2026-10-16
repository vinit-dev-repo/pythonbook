scores = np.array([[80, 90, 70], [60, 85, 95]])

print(scores.sum())
print(scores.mean())
print(scores.std())     # standard deviation: how spread out the values are
print(scores.min())
print(scores.max())
print(scores.argmin())  # position of the smallest value, counting flattened
print(scores.argmax())  # position of the largest value, counting flattened
