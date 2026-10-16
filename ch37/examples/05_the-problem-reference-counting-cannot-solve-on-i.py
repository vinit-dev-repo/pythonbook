import gc

class Node:
    def __init__(self):
        self.other = None

gc.collect()           # establish a baseline before making this demonstration
was_enabled = gc.isenabled()
gc.disable()           # stop automatic passes while this pair is prepared
try:
    a = Node()
    b = Node()
    a.other = b         # a points at b
    b.other = a         # and b points back at a - a cycle
    del a, b            # nothing outside points at either one now

    reported = gc.collect()
    print("reported count at least two:", reported >= 2)
finally:
    if was_enabled:
        gc.enable()
