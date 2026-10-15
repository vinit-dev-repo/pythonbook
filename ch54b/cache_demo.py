# cache_demo.py
from fake_transport import FakeResponse, QueueTransport, scripted_counter
from resource_cache import Resource


if __name__ == '__main__':
    transport = QueueTransport([FakeResponse(b'alpha'), FakeResponse(b'updated'),
                                RuntimeError('offline'), FakeResponse(b'')])
    counter = scripted_counter([10.0, 12.0, 20.0, 20.5, 30.0, 40.0, 40.25])
    resource = Resource('first', transport=transport, counter=counter)
    print('absent:', resource.snapshot, len(transport.calls), len(counter.calls))
    assert resource.body == b'alpha'
    print('loaded:', tuple(resource.snapshot), len(transport.calls), len(counter.calls))
    saved = resource.snapshot
    assert (resource.size, resource.duration, resource.body) == (5, 2.0, b'alpha')
    assert resource.snapshot is saved
    print('reused:', tuple(resource.snapshot), len(transport.calls), len(counter.calls))
    refreshed = resource.refresh()
    assert refreshed is resource.snapshot and refreshed is not saved
    print('refreshed:', tuple(refreshed), len(transport.calls), len(counter.calls))
    try:
        resource.refresh()
    except RuntimeError:
        assert resource.snapshot is refreshed
        assert tuple(resource.snapshot) == ('first', b'updated', 7, 0.5)
        print('failed; retained:', tuple(resource.snapshot), len(transport.calls), len(counter.calls))
    else:
        raise AssertionError('refresh unexpectedly succeeded')
    resource.url = 'second'
    assert resource.snapshot is None
    print('changed; absent:', resource.snapshot, len(transport.calls), len(counter.calls))
    assert (resource.body, resource.size, resource.duration) == (b'', 0, 0.25)
    print('empty loaded:', tuple(resource.snapshot), len(transport.calls), len(counter.calls))
    assert transport.calls == [('first', (3, 10))] * 3 + [('second', (3, 10))]
