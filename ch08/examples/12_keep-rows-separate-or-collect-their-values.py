flat = []
for row in readings:
    for value in row:
        flat.append(value + 1)
print(flat)
