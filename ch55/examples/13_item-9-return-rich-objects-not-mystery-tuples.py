from typing import NamedTuple

class UserInfo(NamedTuple):
    name: str
    age: int
    active: bool

def load_user():
    return UserInfo("Ana", 30, True)

user = load_user()
print(user.name, user.age)
