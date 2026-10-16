def full_crates(items, capacity):
    """Count completely filled crates.

    >>> full_crates(23, 6)
    3
    >>> full_crates(0, 6)
    0
    >>> full_crates(23, 0)
    Traceback (most recent call last):
        ...
    ValueError: use nonnegative items and positive capacity
    """
    if type(items) is not int or type(capacity) is not int:
        raise TypeError("items and capacity must be integers")
    if items < 0 or capacity <= 0:
        raise ValueError("use nonnegative items and positive capacity")
    return items // capacity
