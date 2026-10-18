# development_decoration.py
def development_only(decorate):
    if __debug__:
        return decorate
    return lambda obj: obj

def mark_diagnostic(cls):
    cls.diagnostic = True
    return cls

@development_only(mark_diagnostic)
class Draft:
    pass

print(__debug__)
print(hasattr(Draft, "diagnostic"))
print(type(Draft()).__name__)
