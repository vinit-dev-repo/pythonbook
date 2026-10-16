def add_flag(cls):
    cls.flag = "added"
    return cls

@add_flag
class ReadyBadge:
    pass

print(ReadyBadge.flag)
print(ReadyBadge().__class__ is ReadyBadge)
