# cache_transfer.py
from fake_transport import FakeResponse, QueueTransport, scripted_counter
from resource_cache import Resource


if __name__ == '__main__':
    transport = QueueTransport([FakeResponse(b'left'), FakeResponse(b'right!'),
                                RuntimeError('offline'), FakeResponse(b''), FakeResponse(b'new-right')])
    left_counter = scripted_counter([1.0, 1.5, 2.0, 3.0, 3.25])
    right_counter = scripted_counter([10.0, 11.0, 20.0, 20.75])
    left = Resource('left-v1', transport=transport, counter=left_counter)
    right = Resource('right-v1', transport=transport, counter=right_counter)
    assert left.body == b'left' and right.body == b'right!'
    retained_right = right.snapshot
    print('initial:', tuple(left.snapshot), tuple(right.snapshot))
    left.url = 'left-v2'
    assert left.snapshot is None
    try:
        left.body
    except RuntimeError:
        assert left.snapshot is None
        assert right.snapshot is retained_right
        assert len(transport.calls) == 3 and len(right_counter.calls) == 2
        print('left failed; right retained:', tuple(right.snapshot), len(transport.calls))
    else:
        raise AssertionError('first replacement load unexpectedly succeeded')
    assert left.body == b''
    empty_left = left.snapshot
    assert tuple(empty_left) == ('left-v2', b'', 0, 0.25)
    assert right.snapshot is retained_right and tuple(retained_right) == ('right-v1', b'right!', 6, 1.0)
    print('left recovered:', tuple(left.snapshot), len(transport.calls))
    new_right = right.refresh()
    assert new_right is right.snapshot and new_right is not retained_right
    assert tuple(new_right) == ('right-v1', b'new-right', 9, 0.75)
    assert left.snapshot is empty_left
    assert (left.body, left.size, left.duration) == (b'', 0, 0.25)
    assert (right.body, right.size, right.duration) == (b'new-right', 9, 0.75)
    assert tuple(retained_right) == ('right-v1', b'right!', 6, 1.0)
    print('right refreshed:', tuple(right.snapshot), len(transport.calls))
    assert transport.calls == [('left-v1', (3, 10)), ('right-v1', (3, 10)),
                               ('left-v2', (3, 10)), ('left-v2', (3, 10)), ('right-v1', (3, 10))]
    assert (len(left_counter.calls), len(right_counter.calls)) == (5, 4)
    print('counter calls:', len(left_counter.calls), len(right_counter.calls))
