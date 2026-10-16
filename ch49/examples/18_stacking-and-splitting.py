grid_a = np.array([[1, 2], [3, 4]])
grid_b = np.array([[5, 6], [7, 8]])

print(np.concatenate([grid_a, grid_b], axis=0))   # stacks rows (grows downward)
print(np.concatenate([grid_a, grid_b], axis=1))   # stacks columns (grows sideways)
