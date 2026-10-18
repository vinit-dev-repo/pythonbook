# halves.py
def halve(n):
    """Return half of n.

    >>> halve(8)
    4.0
    >>> halve(0)
    0.0
    >>> halve("8")
    Traceback (most recent call last):
        ...
    TypeError: n must be a number
    """
    if isinstance(n, bool) or not isinstance(n, (int, float)):
        raise TypeError("n must be a number")
    return n / 2
