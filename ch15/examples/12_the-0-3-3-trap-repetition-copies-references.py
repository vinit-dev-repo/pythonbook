inner = []
item = (inner,)
repeated = [item] * 2
repeated[0][0].append(7)
print(repeated)
print(repeated[0][0] is repeated[1][0])
