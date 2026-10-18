class RangeError(ValueError):
    def __init__(self, value, lower, upper):
        super().__init__("Level is outside the allowed inclusive range")
        self.value = value
        self.lower = lower
        self.upper = upper

def validate_level(value):
    if type(value) is not int:
        raise TypeError("Level must be a built-in integer")
    if not 20 <= value <= 30:
        raise RangeError(value, 20, 30)
    return value
