class Shape:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return "I am a shape"

    @classmethod
    def from_text(cls, text):
        return cls(text.strip())

class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def describe(self):
        return "I am a square"

class Label(Shape):
    pass

# 1 and 2
square = Square("Sq1", 4)
print(square.describe())                       # I am a square
print(square.name, square.side)                # Sq1 4

# 3
print(isinstance(square, Shape))               # True
print(type(square) is Shape)                   # False
print(issubclass(Square, Shape))               # True

# 4
label = Label.from_text("  logo  ")
print(type(label).__name__, label.name)        # Label logo
