def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)     # recurse into the nested list
        else:
            yield item

data = [1, [2, 3, [4, 5]], 6, [7]]
print(list(flatten(data)))
