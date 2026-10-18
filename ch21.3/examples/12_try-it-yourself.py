# 1
class Dog:
    pass

print(callable(Dog))               # True
print(callable(Dog()))             # False
print(type(Dog))                   # <class 'type'>

# 2
print(type(5))                     # <class 'int'>
print(type(int))                   # <class 'type'>
print(isinstance(5, int))          # True
print(isinstance(int, type))       # True

# 3
class Note:
    def __init__(self, title):
        self.title = title

note = Note("first")
note.color = "teal"
print(vars(note))                  # {'title': 'first', 'color': 'teal'}
note.colour = "blue"               # a typo: no error
print(vars(note))                  # {'title': 'first', 'color': 'teal', 'colour': 'blue'}

# 4
print(getattr(note, "size", "no size"))    # no size
setattr(note, "size", 3)
print(note.size)                           # 3
delattr(note, "size")
try:
    print(note.size)
except AttributeError as error:
    print(type(error).__name__)            # AttributeError
try:
    print(vars(note)["size"])
except KeyError as error:
    print(type(error).__name__)            # KeyError

# 5
class Formatter:
    shout = staticmethod(str.upper)

print(Formatter.shout("hello"))            # HELLO
print(Formatter().shout("hello"))          # HELLO
