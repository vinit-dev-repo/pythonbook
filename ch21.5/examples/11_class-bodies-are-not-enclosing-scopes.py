class Config2:
    factor = 10
    values = [1, 2, 3]
    scaled = []
    for v in values:
        scaled.append(v * factor)

print(Config2.scaled)
