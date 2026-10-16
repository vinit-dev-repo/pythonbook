events = []

class ParcelScope:
    def __init__(self, name, *, fail_entry=False, fail_exit=False):
        self.name = name
        self.fail_entry = fail_entry
        self.fail_exit = fail_exit
        self.active = False

    def __enter__(self):
        events.append(f"enter {self.name}")
        self.active = True             # a simulated acquisition
        if self.fail_entry:
            self.active = False        # entry owns its partial cleanup
            events.append(f"undo {self.name}")
            raise LookupError("setup failed")
        return (self.name,)             # the value is not this manager

    def __exit__(self, kind, error, traceback):
        self.active = False
        label = "ok" if kind is None else kind.__name__
        events.append(f"exit {self.name}: {label}")
        if self.fail_exit:
            raise OSError("cleanup failed")
        return False

outer = ParcelScope("outer")
inner = ParcelScope("inner", fail_entry=True)
try:
    with outer, inner:
        raise AssertionError("body must not run")
except LookupError:
    pass
print(events)
assert not outer.active and not inner.active

events.clear()
try:
    with ParcelScope("binding") as (first, second):
        raise AssertionError("binding must fail first")
except ValueError:
    pass
print(events)

events.clear()
body_error = ValueError("body failed")
try:
    with ParcelScope("cleanup", fail_exit=True):
        raise body_error
except OSError as error:
    assert error.__context__ is body_error
    print(type(error).__name__, type(error.__context__).__name__)
print(events)
