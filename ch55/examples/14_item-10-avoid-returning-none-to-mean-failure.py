from typing import Optional

def find_user(users, name) -> Optional[dict]:
    for user in users:
        if user["name"] == name:
            return user
    return None   # explicit: caller's type hint says "might be missing"

users = [{"name": "Ana"}]
result = find_user(users, "Bob")
if result is None:
    print("No such user")
else:
    print(result)
