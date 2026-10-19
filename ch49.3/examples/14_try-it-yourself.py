import numpy as np

# 3
scores = np.array([[2, 4, 6], [1, 5, 9]])
means = scores.mean(axis=1).reshape(2, 1)
centered = scores - means
print(centered.tolist())
print(centered.sum(axis=1).tolist())
