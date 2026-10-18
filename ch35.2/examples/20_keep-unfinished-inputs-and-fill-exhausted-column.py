def rows_longest(*sources, fill=None):
    streams = [iter(source) for source in sources]
    remaining = len(streams)
    while remaining:
        row = []
        for position, stream in enumerate(streams):
            if stream is None:
                row.append(fill)
                continue
            try:
                value = next(stream)
            except StopIteration:
                streams[position] = None
                remaining -= 1
                value = fill
            row.append(value)
        if remaining:
            yield tuple(row)

print(list(rows_longest(iter([None, 7]), ["ready"], fill="missing")))
print(list(rows_longest([], [], fill="missing")))
print(list(rows_longest()))
