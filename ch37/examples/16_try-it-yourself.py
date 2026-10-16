# 2
import gc

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
