class ConversionError(ValueError):
    pass

def bool_from_integer(value):
    if type(value) not in (bool, int):
        raise TypeError("Integer helper does not support this type")
    if value not in (0, 1):
        raise ValueError("Integer value must be 0 or 1")
    return bool(value)

def bool_from_text(value):
    if type(value) is not str:
        raise TypeError("Text helper does not support this type")
    tokens = {"0": False, "f": False, "false": False,
              "1": True, "t": True, "true": True}
    key = value.casefold()
    if key not in tokens:
        raise ValueError("Text must be 0, 1, t, f, true or false")
    return tokens[key]

def convert_bool(value):
    try:
        return bool_from_integer(value)
    except ValueError as original:
        raise ConversionError("Invalid Boolean value") from original
    except TypeError:
        pass  # Try the text helper only for an unsupported type.
    try:
        return bool_from_text(value)
    except (TypeError, ValueError) as original:
        raise ConversionError("Cannot convert this Boolean setting") from original

for value in (False, True, 0, 1, "T", "false", "1", 10, "ABC", 1.0, ""):
    try:
        print(repr(value), "->", convert_bool(value))
    except ConversionError as error:
        print(repr(value), "->", type(error).__name__,
              "caused by", type(error.__cause__).__name__)
