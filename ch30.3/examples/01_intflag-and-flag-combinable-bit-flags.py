from enum import IntFlag, auto

class Permission(IntFlag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

user_perms = Permission.READ | Permission.WRITE
print(user_perms)
print(repr(user_perms))            # the name view, if you want to see it
print(Permission.READ in user_perms)
print(Permission.EXECUTE in user_perms)
