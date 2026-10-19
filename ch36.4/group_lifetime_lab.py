# group_lifetime_lab.py
from itertools import compress, groupby, tee

def report(groups):
    return [(key, sum(1 for _ in group)) for key, group in groups]

def main():
    rows = [("S1", "Pine", "S1"), ("S2", "Cedar", "S2")]
    used_mask = iter((True, True, False))
    print("spent mask:", [tuple(compress(row, used_mask)) for row in rows])
    mask = (True, True, False)
    print("saved mask:", [tuple(compress(row, mask)) for row in rows])

    values = ["Cedar", "Cedar", "Pine"]
    first, second = tee(groupby(values))
    left = next(first)
    right = next(second)
    print("same inner iterator:", left[1] is right[1])
    print("first consumer:", list(left[1]))
    print("second consumer:", list(right[1]))

    first, second = tee(groupby(values))
    print("unfixed:", report(first), report(second))
    print("fresh groups:", report(groupby(values)), report(groupby(values)))

    # Freeze each count while its group is still current, then tee values.
    counts = ((key, sum(1 for _ in group)) for key, group in groupby(values))
    first, second = tee(counts)
    print("tee counts:", list(first), list(second))

if __name__ == "__main__":
    main()
