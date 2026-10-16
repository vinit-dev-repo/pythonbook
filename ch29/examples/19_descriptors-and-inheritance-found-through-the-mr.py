class Positive:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        print(f"  (Positive.__get__ ran, reached via {objtype.__name__})")
        return getattr(obj, self._name)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self._name[1:]} must be positive")
        setattr(obj, self._name, value)

class Shape:
    size = Positive()

    def __init__(self, size):
        self.size = size

class Square(Shape):
    pass

class TinySquare(Square):
    pass

t = TinySquare(4)
print(t.size)
print([c.__name__ for c in TinySquare.__mro__])
print("size" in vars(Shape), "size" in vars(Square), "size" in vars(TinySquare))
print(vars(t))
