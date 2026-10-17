readings = [[12, 15, 9], [], [8, 11, 4]]
kept = [value for row in readings if row for value in row if value >= 10]
print(kept)
