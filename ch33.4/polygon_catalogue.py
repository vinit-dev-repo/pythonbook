# polygon_catalogue.py
from dataclasses import dataclass, field, FrozenInstanceError
from functools import cached_property
import math


def check_dimensions(sides, radius):
    if type(sides) is not int:
        raise TypeError("sides must be an integer, not bool")
    if not 3 <= sides <= 100_000:
        raise ValueError("this lab supports 3 through 100000 sides")
    if type(radius) not in (int, float):
        raise TypeError("radius must be int or float, not bool")
    if not 1e-6 <= radius <= 1e6:
        raise ValueError("this lab supports radii from 1e-6 through 1e6")


@dataclass(frozen=True)
class Polygon:
    sides: int
    radius: float

    def __post_init__(self):
        check_dimensions(self.sides, self.radius)

    @property
    def vertices(self):
        return self.sides

    @property
    def interior_angle(self):
        return 180 - 360 / self.sides

    @property
    def side_length(self):
        return 2 * self.radius * math.sin(math.pi / self.sides)

    @property
    def apothem(self):
        return self.radius * math.cos(math.pi / self.sides)

    @property
    def perimeter(self):
        return self.sides * self.side_length

    @property
    def area(self):
        return self.perimeter * self.apothem / 2

    def __gt__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return self.sides > other.sides


@dataclass(frozen=True)
class CachedPolygon(Polygon):
    interior_angle = cached_property(Polygon.interior_angle.fget)
    side_length = cached_property(Polygon.side_length.fget)
    apothem = cached_property(Polygon.apothem.fget)
    perimeter = cached_property(Polygon.perimeter.fget)
    area = cached_property(Polygon.area.fget)


def area_per_boundary(shape):
    return shape.area / shape.perimeter


@dataclass(frozen=True)
class PolygonShelf:
    limit: int
    radius: float
    _items: tuple = field(init=False, repr=False, compare=False)

    def __post_init__(self):
        check_dimensions(self.limit, self.radius)
        items = tuple(Polygon(n, self.radius)
                      for n in range(3, self.limit + 1))
        object.__setattr__(self, "_items", items)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, key):
        return self._items[key]

    @property
    def best(self):
        return max(self, key=area_per_boundary)


@dataclass(frozen=True)
class PolygonWalk:
    limit: int
    radius: float

    def __post_init__(self):
        check_dimensions(self.limit, self.radius)

    def __len__(self):
        return self.limit - 2

    def __iter__(self):
        return PolygonCursor(self.limit, self.radius)

    @property
    def best(self):
        return max(self, key=area_per_boundary)


@dataclass
class PolygonCursor:
    limit: int
    radius: float
    _remaining: object = field(init=False, repr=False)

    def __post_init__(self):
        check_dimensions(self.limit, self.radius)
        self._remaining = iter(range(3, self.limit + 1))

    def __iter__(self):
        return self

    def __next__(self):
        sides = next(self._remaining)
        return CachedPolygon(sides, self.radius)


def check_polygon(kind):
    # Square with diagonals of length 10; no trig formula in this oracle.
    square = kind(4, 5)
    assert square.vertices == square.sides == 4
    assert square.radius == 5
    assert repr(square) == f"{kind.__qualname__}(sides=4, radius=5)"
    for attribute, expected in (
        ("interior_angle", 90), ("side_length", math.sqrt(50)),
        ("apothem", math.sqrt(12.5)), ("perimeter", 4 * math.sqrt(50)),
        ("area", 50),
    ):
        assert math.isclose(getattr(square, attribute), expected,
                            rel_tol=1e-12, abs_tol=1e-12), attribute
    assert kind(5, 3) == kind(5, 3)
    assert kind(5, 3) != kind(5, 4)
    assert kind(5, 3) != kind(6, 3)
    assert kind(5, 3) < kind(6, 1)  # reflected __gt__
    assert not kind(5, 3) > kind(5, 4)
    assert not kind(5, 3) < kind(5, 4)
    assert kind.__gt__(square, 4) is NotImplemented
    try:
        kind(2, 5)
    except ValueError:
        pass
    else:
        raise AssertionError("two sides must be rejected")
    try:
        square.radius = 8
    except FrozenInstanceError:
        pass
    else:
        raise AssertionError("public dimensions must stay fixed")


def diagnose_failures():
    class UncheckedPolygon(Polygon):
        def __post_init__(self):
            pass

    class WrongScope(Polygon):
        @property
        def interior_angle(self):
            return 180 - 360 / missing_sides

    class MissingReturn(CachedPolygon):
        @cached_property
        def area(self):
            value = Polygon.area.fget(self)  # deliberately no return

    for kind, expected in ((UncheckedPolygon, AssertionError),
                           (WrongScope, NameError),
                           (MissingReturn, TypeError)):
        try:
            check_polygon(kind)
        except expected as error:
            if kind is UncheckedPolygon:
                assert str(error) == "two sides must be rejected"
            print(kind.__name__ + ":", expected.__name__)
        else:
            raise AssertionError("the planted defect escaped its check")
    try:
        assert repr(Polygon(4, 5)) == "Polygon(sides=4,radius=5)"
    except AssertionError:
        print("bad repr expectation: AssertionError")


if __name__ == "__main__":
    diagnose_failures()
    for kind in (Polygon, CachedPolygon):
        check_polygon(kind)
    print("same geometry checks: PASS")
    shelf = PolygonShelf(7, 5)
    print("shelf:", len(shelf), [p.sides for p in shelf[::-2]])
    walk = PolygonWalk(7, 5)
    first, second = iter(walk), iter(walk)
    print("independent:", next(first).sides, next(first).sides,
          next(second).sides)
    print("rest:", [p.sides for p in first])
    print("exhausted:", list(first))
    print("fresh:", [p.sides for p in walk])
    shape = next(iter(walk))
    print("cache before:", sorted(vars(shape)))
    _ = shape.area
    print("cache after area:", sorted(vars(shape)))
    print("best:", shelf.best.sides, walk.best.sides)
