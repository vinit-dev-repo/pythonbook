# route_transfer.py
from attribute_policy import Public


class Route:
    def __init__(self, stops):
        self.stops = list(stops)

    def __getitem__(self, index):
        return self.stops[index]

    def __iter__(self):
        return iter(self.stops)


def make_route_policy(*allowed_names):
    base = Public(*allowed_names)(Route)

    class RoutePolicy(base):
        def __getitem__(self, index):
            return self.__getattr__('__getitem__')(index)

        def __iter__(self):
            return self.__getattr__('__iter__')()

    return RoutePolicy


ReadRoute = make_route_policy('__getitem__', '__iter__')
NoIndex = make_route_policy('__iter__')


if __name__ == '__main__':
    stops = ['A', 'B']
    route = ReadRoute(stops)
    stops.append('C')
    assert route[0] == 'A' and list(route) == ['A', 'B']
    first = iter(route)
    second = iter(route)
    assert first is not second
    assert iter(first) is first
    print('route independent:', next(first), next(second), next(first))

    no_index = NoIndex(['A', 'B'])
    for operation in (lambda: no_index.__getitem__(0), lambda: no_index[0]):
        try:
            operation()
        except TypeError as error:
            assert str(error) == 'access denied: __getitem__'
        else:
            raise AssertionError('indexing should be denied')
    print('route denied index: explicit and implicit')
    assert list(no_index) == ['A', 'B']
    print('route permitted iteration:', list(iter(no_index)))
