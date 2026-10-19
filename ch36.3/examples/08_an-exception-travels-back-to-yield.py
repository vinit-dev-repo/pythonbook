from contextlib import contextmanager

@contextmanager
def recorded_scope(log, *, handle_lookup=False):
    log.append("enter")
    try:
        yield {"ready": True}
    except LookupError:
        log.append("caught lookup")
        if not handle_lookup:
            raise
    finally:
        log.append("exit")

log = []
with recorded_scope(log, handle_lookup=True) as value:
    assert value == {"ready": True}
    raise KeyError("missing parcel")
print(log)

log.clear()
original = KeyError("still missing")
try:
    with recorded_scope(log):
        raise original
except KeyError as error:
    assert error is original
print(log)

@recorded_scope(log)
def labelled(number):
    return f"parcel-{number}"

log.clear()
print(labelled(1), labelled(2))
print(log)
