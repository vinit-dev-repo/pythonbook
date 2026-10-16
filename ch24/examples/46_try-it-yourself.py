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

# 1 and 2
try:
    raise ShapeError("Something is wrong with this shape")
except ShapeError as e:
    print(e)

try:
    make_circle(-5)
except InvalidRadiusError as e:
    print(e, "-", e.radius)

# 3
for value in (-2, 3):
    try:
        print(make_circle(value))
    except ShapeError as e:
        print("Caught:", e)

# 4
def safe_divide_area(total, sides):
    try:
        return total / sides
    except ZeroDivisionError as original:
        raise ShapeError("A shape needs at least one side") from original

try:
    safe_divide_area(10, 0)
except ShapeError as e:
    print("Caught:", e)

# 5
class AppError(Exception):
    pass

class ValidationError(AppError):
    pass

try:
    raise ValidationError("bad value")
except AppError as e:
    print("Caught as AppError:", e)

# Also exercise the second ShapeError subclass from task 3.
try:
    raise InvalidSidesError(0)
except ShapeError as e:
    print("Caught sibling:", e)

# Inspect the explicit cause retained in task 4.
try:
    safe_divide_area(10, 0)
except ShapeError as e:
    print("Original cause:", type(e.__cause__).__name__)
