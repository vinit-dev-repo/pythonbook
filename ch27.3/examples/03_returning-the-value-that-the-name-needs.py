def add_flag_but_forget_return(cls):
    cls.flag = "added"

@add_flag_but_forget_return
class BrokenBadge:
    pass

print(BrokenBadge is None)
try:
    BrokenBadge()
except TypeError as error:
    print(type(error).__name__)
