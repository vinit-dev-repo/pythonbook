# 4
rows = [[0] * 2] * 2
rows[0][1] = 9
print(rows)

rows = [[0] * 2 for _ in range(2)]
rows[0][1] = 9
print(rows)

rows = [([],) for _ in range(2)]
rows[0][0].append('x')
print(rows)
