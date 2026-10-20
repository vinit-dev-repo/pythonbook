# 3
from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    name: str
    admin: bool
    active: bool


def make_user(name, *, admin=False, active=True):
    if not isinstance(name, str):
        raise TypeError(f"name must be str, got {type(name).__name__}")
    if not name.strip():
        raise ValueError("name must not be empty")
    return User(name.strip(), admin, active)


calls = [
    lambda: make_user("Ana"),
    lambda: make_user("Ben", admin=True),
    lambda: make_user("Cy", True),
    lambda: make_user("  "),
    lambda: make_user(7),
]
for call in calls:
    try:
        print(call())
    except (TypeError, ValueError) as error:
        print(type(error).__name__ + ":", error)
