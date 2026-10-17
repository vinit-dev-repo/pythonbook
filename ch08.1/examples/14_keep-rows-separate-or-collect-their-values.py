rows = []
for row in readings:
    new_row = []
    for value in row:
        new_row.append(value + 1)
    rows.append(new_row)
print(rows)
