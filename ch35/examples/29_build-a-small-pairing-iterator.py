def rows_shortest(*sources):
    streams = [iter(source) for source in sources]
    if not streams:
        return
    while True:
        row = []
        for stream in streams:
            try:
                value = next(stream)
            except StopIteration:
                return
            row.append(value)
        yield tuple(row)

numbers = iter([4, 7, 9])
print(list(rows_shortest(numbers, ["ready"])))
print("unused:", list(numbers))
print("no inputs:", list(rows_shortest()))
print("one input:", list(rows_shortest([4, 7])))
