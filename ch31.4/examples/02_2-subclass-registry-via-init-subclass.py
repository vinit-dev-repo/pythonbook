class Shape:
    registry = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Shape.registry.append(cls.__name__)

class Circle(Shape):
    pass

class Square(Shape):
    pass

print(Shape.registry)
