import gc
import weakref

class DeliveryNote:
    def __init__(self, code):
        self.code = code

released = []
note = DeliveryNote("R8")
watch = weakref.ref(note)
finished = weakref.finalize(note, released.append, note.code)
alias = note
del note
held = watch()
print(held is alias, finished.alive)
del alias
gc.collect()
print(watch() is held, released)
del held
gc.collect()
print(watch() is None, finished.alive, released)
print(finished())
