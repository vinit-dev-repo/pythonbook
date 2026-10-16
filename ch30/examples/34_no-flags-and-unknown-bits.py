from enum import Flag, IntFlag, auto

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

class RawPermission(IntFlag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

empty = Permission(0)
print(bool(empty), Permission.READ in empty)
try:
    Permission(8)
except ValueError as error:
    print("unknown Flag bit:", type(error).__name__)
raw = RawPermission(8)
print("preserved IntFlag value:", int(raw))
