def add_debug_state(cls):
    def debug_state(self):
        return f"{type(self).__name__}: {vars(self)}"

    cls.debug_state = debug_state
    return cls

class Draft:
    def __init__(self, title):
        self.title = title

draft = Draft("First")
Draft = add_debug_state(Draft)

@add_debug_state
class Meter:
    def __init__(self, reading):
        self.reading = reading

print(draft.debug_state())
meter = Meter(4)
print(meter.debug_state())
meter.reading = 9
print(meter.debug_state())
