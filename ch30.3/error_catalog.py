# error_catalog.py
from enum import Enum, unique

@unique
class Catalog(Enum):
    BAD_NAME = (100, ValueError, "name is required")
    ACCESS_DENIED = (200, PermissionError, "access denied")

    def __new__(cls, code, exception_type, default_message):
        member = object.__new__(cls)
        member._value_ = code
        member.exception_type = exception_type
        member.default_message = default_message
        return member

    @property
    def code(self):
        return self.value

    def throw(self, message=None):
        if message is None:
            message = self.default_message
        elif not isinstance(message, str):
            raise TypeError("message must be str or None")
        raise self.exception_type(message)

if __name__ == "__main__":
    by_code = Catalog(100)
    print("identity:", by_code is Catalog.BAD_NAME)
    print("name lookup:", Catalog["BAD_NAME"] is by_code)
    for item in Catalog:
        print(item.name, item.code, item.exception_type.__name__, item.default_message)
    for lookup in (lambda: Catalog(999), lambda: Catalog["MISSING"]):
        try:
            lookup()
        except (ValueError, KeyError) as error:
            print(type(error).__name__)
