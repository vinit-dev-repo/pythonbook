# pool_transfer.py
from bingoaddable import AddableBingoCage
from tombolist import TomboList


def drain_by_call(pool):
    values = []
    while True:
        try:
            values.append(pool())
        except LookupError:
            return tuple(sorted(values))


if __name__ == '__main__':
    original = AddableBingoCage([8, 8, 6])
    alias = original
    old_snapshot = original.inspect()
    registered = TomboList([7, 8])
    combined = original + registered
    combined_snapshot = combined.inspect()
    assert combined is not original and combined is not registered
    assert combined_snapshot == (6, 7, 8, 8, 8)
    extension = (ticket for ticket in (5, 5))
    original += extension
    assert tuple(extension) == ()
    assert original is alias
    assert old_snapshot == (6, 8, 8)
    assert original.inspect() == (5, 5, 6, 8, 8)
    assert registered.inspect() == (7, 8)
    assert combined.inspect() == combined_snapshot
    drawn = drain_by_call(combined)
    assert drawn == combined_snapshot
    assert combined.loaded() is False
    print('identities:', original is alias, combined is original, combined is registered)
    print('old snapshot:', old_snapshot)
    print('original after extension:', original.inspect())
    print('registered unchanged:', registered.inspect())
    print('combined draws:', drawn)
    try:
        combined()
    except LookupError as error:
        print('combined exhausted:', type(error).__name__)
    else:
        raise AssertionError('exhausted call must fail')
