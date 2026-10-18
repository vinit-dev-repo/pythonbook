class ShapeError(Exception):
    pass

class InvalidRadiusError(ShapeError):
    def __init__(self, radius):
        super().__init__(f"Invalid radius: {radius}")
        self.radius = radius

class InvalidSidesError(ShapeError):
    def __init__(self, sides):
        super().__init__(f"Invalid number of sides: {sides}")
        self.sides = sides

def make_circle(radius):
    if radius < 0:
        raise InvalidRadiusError(radius)
    return f"Circle(radius={radius})"

# 1
try:
    make_circle(-5)
except InvalidRadiusError as error:
    print(error, "-", error.radius)            # Invalid radius: -5 - -5

# 2
for value in (-2, 3):
    try:
        print(make_circle(value))
    except ShapeError as error:
        print("Caught:", error)
# Caught: Invalid radius: -2
# Circle(radius=3)

try:
    raise InvalidSidesError(0)
except ShapeError as error:
    print("Caught sibling:", error)            # Caught sibling: Invalid number of sides: 0

# 3
try:
    raise InvalidRadiusError(-1)
except ShapeError:
    print("family handler first")              # family handler first
except InvalidRadiusError:
    print("never printed")
