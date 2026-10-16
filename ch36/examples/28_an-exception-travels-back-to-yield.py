@contextmanager
def no_value():
    yield from ()

@contextmanager
def two_values():
    yield "first"
    yield "second"

for factory in (no_value, two_values):
    entered_body = False
    try:
        with factory():
            entered_body = True
    except RuntimeError:
        print(factory.__name__, entered_body)
