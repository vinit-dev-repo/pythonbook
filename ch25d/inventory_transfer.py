# inventory_transfer.py
from app.models.devices import SSD


def stock(item):
    return item.total, item.allocated, item.available


if __name__ == '__main__':
    main = SSD('Archive', 'Acme', 6, 1, 512, 'SATA')
    other = SSD('Spare', 'Acme', 2, 0, 256, 'USB')
    other_before = vars(other).copy()
    assert stock(main) == (6, 1, 5)
    print('start:', stock(main))
    for action, amount, expected in [('claim', 3, (6, 4, 2)), ('freeup', 2, (6, 2, 4)),
                                     ('died', 1, (5, 1, 4)), ('purchased', 2, (7, 1, 6))]:
        assert getattr(main, action)(amount) is None
        assert stock(main) == expected
        assert vars(other) == other_before
        print(action, amount, stock(main))
    before = (stock(main), vars(main).copy())
    try:
        main.claim(7)
    except ValueError:
        assert (stock(main), vars(main)) == before
        print('rejected; unchanged:', stock(main))
    else:
        raise AssertionError('over-allocation succeeded')
    assert (main.name, main.manufacturer, main.capacity_gb, main.interface, main.category, str(main)) == ('Archive', 'Acme', 512, 'SATA', 'ssd', 'Archive')
    assert repr(main) == "Storage(category='ssd', name='Archive', capacity_gb=512, interface='SATA')"
    assert vars(other) == other_before and stock(other) == (2, 0, 2)
    print(repr(main))
    print('other unchanged:', stock(other))
