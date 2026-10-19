import gc
import weakref

# 1
class Node:
    def __init__(self):
        self.other = None

gc.collect()
was_enabled = gc.isenabled()
gc.disable()
try:
    a = Node()
    b = Node()
    a.other, b.other = b, a
    del a, b
    print(gc.collect() >= 2)
finally:
    if was_enabled:
        gc.enable()

# 2
class Greeting:
    def __init__(self, text):
        self.text = text

    def __del__(self):
        print(f"Goodbye from: {self.text}")

message = Greeting("hello")
saved = message
message = "something else"
print("after rebinding message")
del saved
print("after del saved")

# 3
class Note:
    pass

note = Note()
watch = weakref.ref(note)
alias = note
del note
gc.collect()
print(watch() is alias)
del alias
gc.collect()
print(watch() is None)

# 4
class RowList(list):
    pass

rows = RowList()
print(weakref.ref(rows)() is rows)
try:
    weakref.ref([])
except TypeError:
    print("a plain list does not support weak references")
