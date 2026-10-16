class IntConversion:
    def __int__(self):
        return 1

class WrongIndex:
    def __index__(self):
        return 1.5

print(int(IntConversion()))
try:
    print("abc"[IntConversion()])
except TypeError:
    print("TypeError: __int__ alone is not an index")
try:
    print("abc"[WrongIndex()])
except TypeError:
    print("TypeError: __index__ returned a non-integer")
