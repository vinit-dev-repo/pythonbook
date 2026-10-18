def make_reading_pair():
    def read():
        nonlocal current
        return current
    def advance():
        nonlocal current
        current += 3
        return current
    current = 10
    return read, advance

read_value, advance_value = make_reading_pair()
print(read_value(), advance_value(), read_value())
