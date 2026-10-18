# 1
class ShapeError(Exception):
    pass

try:
    raise ShapeError("Something is wrong with this shape")
except ShapeError as error:
    print(error)                               # Something is wrong with this shape

# 2
class AppError(Exception):
    pass

class ValidationError(AppError):
    pass

try:
    raise ValidationError("bad value")
except AppError as error:
    print("Caught as AppError:", error)        # Caught as AppError: bad value

# 3
try:
    b"\xff".decode("utf-8")
except ValueError as error:
    print(type(error).__name__)                # UnicodeDecodeError

# 4
try:
    1 / 0
except Exception as error:
    print(type(error).__name__)                # ZeroDivisionError
print(issubclass(ZeroDivisionError, Exception))      # True
print(issubclass(KeyboardInterrupt, Exception))      # False
