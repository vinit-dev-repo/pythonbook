import inspect

def relay_plain():
    result = yield from [10, 20]
    return result

plain = relay_plain()
print(next(plain), plain.send(None))
try:
    next(plain)
except StopIteration as done:
    print("ordinary result:", done.value)

plain = relay_plain()
next(plain)
try:
    plain.send(99)
except AttributeError:
    print("no send:", inspect.getgeneratorstate(plain))

log = []
def closable():
    try:
        yield "ready"
    finally:
        log.append("cleanup")

unstarted = closable()
unstarted.close()
print("unstarted:", log)
started = closable()
next(started)
started.close()
print("started:", log)

def refusing_close():
    try:
        yield "ready"
    except GeneratorExit:
        yield "cannot yield during close"

bad = refusing_close()
next(bad)
try:
    bad.close()
except RuntimeError:
    print("bad close:", inspect.getgeneratorstate(bad))
finally:
    bad.close()                    # now suspended outside the handler's try
print("after second close:", inspect.getgeneratorstate(bad))
