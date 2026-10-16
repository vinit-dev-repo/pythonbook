try:
    np.array([1, 2, 3]) + np.array([1, 2])
except ValueError as e:
    print("Error:", str(e).strip())
