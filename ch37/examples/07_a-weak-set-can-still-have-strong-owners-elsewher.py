import gc
import weakref

class Preview:
    live = weakref.WeakSet()

    def __init__(self, title):
        self.title = title
        self.live.add(self)

    def refresh(self):
        return self.title.upper()

first = Preview("outline")
second = Preview("notes")
saved_action = first.refresh
del first
gc.collect()
print(len(Preview.live), saved_action())
del second
gc.collect()
print(len(Preview.live))
del saved_action
gc.collect()
print(len(Preview.live))
