rng = np.random.default_rng(seed=42)
dice_rolls = rng.integers(1, 7, size=5)   # 5 numbers, 1 to 6
print(dice_rolls)
