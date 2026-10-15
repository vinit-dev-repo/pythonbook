# inventory_demo.py
from app.models.devices import CPU, HDD, SSD, Storage
from app.models.resource import Resource


def stock(item):
    return item.total, item.allocated, item.available


if __name__ == '__main__':
    router = Resource(' Router ', ' Acme ', 10, 3)
    print('start:', stock(router))
    for action, amount, expected in [('claim', 2, (10, 5, 5)), ('freeup', 1, (10, 4, 6)),
                                     ('died', 2, (8, 2, 6)), ('purchased', 4, (12, 2, 10))]:
        assert getattr(router, action)(amount) is None
        assert stock(router) == expected
        print(action, amount, stock(router))
    before = vars(router).copy()
    try:
        router.claim(11)
    except ValueError:
        assert vars(router) == before
        print('rejected; unchanged:', stock(router))
    else:
        raise AssertionError('over-allocation succeeded')
    print(repr(router))
    devices = [CPU('Xeon', 'Intel', 4, 1, 8, 'LGA', 95),
               Storage('Disk', 'Seagate', 2, 0, 500),
               HDD('Archive', 'Seagate', 2, 0, 1000, '3.5"', 7200),
               SSD('Flash', 'Acme', 2, 0, 512, 'NVMe')]
    for device in devices:
        print(repr(device))
    empty = Resource('empty', 'Acme', 0, 0)
    empty.purchased(1)
    empty.claim(1)
    assert stock(empty) == (1, 1, 0)
    print('empty after purchase/claim:', stock(empty))
