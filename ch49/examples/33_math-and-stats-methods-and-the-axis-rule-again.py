print(scores.sum(axis=0))    # collapse rows -> one total PER COLUMN
print(scores.sum(axis=1))    # collapse columns -> one total PER ROW
print(scores.mean(axis=0))
print(scores.max(axis=1))
