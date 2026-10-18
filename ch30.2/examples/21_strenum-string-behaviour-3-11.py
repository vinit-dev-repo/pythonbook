from enum import StrEnum

class Role(StrEnum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"

print(Role.ADMIN == "admin")
print(f"Role is {Role.ADMIN}")

import json
print(json.dumps({"role": Role.ADMIN}))
