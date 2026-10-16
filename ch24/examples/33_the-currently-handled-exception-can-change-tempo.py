try:
    raise ValueError("outer")
except ValueError:
    print("Outer:", sys.exc_info()[0].__name__)
    try:
        raise TypeError("inner")
    except TypeError:
        print("Inner:", sys.exc_info()[0].__name__)
    print("Restored:", sys.exc_info()[0].__name__)
print("After:", sys.exc_info())
