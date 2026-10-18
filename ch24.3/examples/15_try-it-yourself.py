# 1
class ShapeError(Exception):
    pass

def safe_divide_area(total, sides):
    try:
        return total / sides
    except ZeroDivisionError as original:
        raise ShapeError("A shape needs at least one side") from original

try:
    safe_divide_area(10, 0)
except ShapeError as error:
    print("Original cause:", type(error.__cause__).__name__)
# Original cause: ZeroDivisionError

# 2
class ConversionError(ValueError):
    pass

def to_number(text, hide=False):
    try:
        return int(text)
    except ValueError as original:
        if hide:
            raise ConversionError("not a number") from None
        raise ConversionError("not a number") from original

try:
    to_number("x")
except ConversionError as error:
    print(type(error.__cause__).__name__)      # ValueError

try:
    to_number("x", hide=True)
except ConversionError as error:
    print(error.__cause__, error.__suppress_context__, type(error.__context__).__name__)
# None True ValueError

# 3
def count_broad(text):
    try:
        return int(txt)
    except Exception:
        return 0

def count_narrow(text):
    try:
        return int(text)
    except ValueError:
        return 0

print(count_broad("5"))                        # 0
print(count_narrow("5"))                       # 5
