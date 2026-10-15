# counter_transfer.py
from hook_insertion import insert_private


class Counter:
    def __init__(self, value):
        self.value = value

    def advance(self):
        self.value += 1
        return self.value


if __name__ == '__main__':
    counter = Counter(2)
    Original = Counter
    original_counter = counter
    inserted = insert_private('value')(Counter)
    assert inserted is Original and type(counter) is Original
    assert counter is original_counter
    saved_advance = counter.advance
    assert saved_advance.__self__ is counter
    print('same class:', inserted is Original, type(counter) is Original)
    print('saved method receiver:', saved_advance.__self__ is counter)
    try:
        saved_advance()
    except TypeError as error:
        assert str(error) == 'private read: value'
        print(f'advance after hook: {type(error).__name__}: {error}')
    else:
        raise AssertionError('advance should fail before increment')
    assert object.__getattribute__(counter, 'value') == 2
    print('raw value unchanged:', object.__getattribute__(counter, 'value'))
