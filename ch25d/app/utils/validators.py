# app/utils/validators.py
def validate_text(name, value):
    if type(value) is not str:
        raise TypeError(f"{name} must be a string")
    value = value.strip()
    if not value:
        raise ValueError(f"{name} must not be blank")
    return value


def validate_integer(
    name,
    value,
    min_value=None,
    max_value=None,
    custom_min_message=None,
    custom_max_message=None,
):
    if type(value) is not int:
        raise TypeError(f"{name} must be an int")
    if min_value is not None and value < min_value:
        message = custom_min_message if custom_min_message is not None else f"{name} must be at least {min_value}"
        raise ValueError(message)
    if max_value is not None and value > max_value:
        message = custom_max_message if custom_max_message is not None else f"{name} must be at most {max_value}"
        raise ValueError(message)
