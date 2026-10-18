from enum import Enum, unique

try:
    @unique
    class DuplicateCatalog(Enum):
        FIRST = (100, ValueError, "first")
        SECOND = (100, PermissionError, "second")

        def __new__(cls, code, exception_type, default_message):
            member = object.__new__(cls)
            member._value_ = code
            member.exception_type = exception_type
            member.default_message = default_message
            return member
except ValueError as error:
    print(type(error).__name__ + ":", error)
