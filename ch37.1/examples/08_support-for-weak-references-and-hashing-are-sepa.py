import weakref

class RowList(list):
    pass

rows = RowList(["draft"])
print(weakref.ref(rows)() is rows)
try:
    weakref.WeakSet([rows])
except TypeError:
    print("weak set members must also be hashable")
try:
    weakref.ref([])
except TypeError:
    print("a plain list does not support weak references")
