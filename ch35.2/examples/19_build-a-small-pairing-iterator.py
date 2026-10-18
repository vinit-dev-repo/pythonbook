def apply_rows(function, *sources):
    if not sources:
        raise TypeError("at least one input is required")
    for row in rows_shortest(*sources):
        yield function(*row)

print(list(apply_rows(lambda label, count: f"{label}:{count}",
                      ["open", "close"], [2, 5])))
