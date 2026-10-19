import inspect


# 1
def running_total():
    total = 0
    while True:
        value = yield total
        total += value


total = running_total()
next(total)
print("sent 5:", total.send(5))
print("sent 3:", total.send(3))


# 2
def logger(log):
    try:
        while True:
            try:
                log.append((yield))
            except ValueError:
                log.append("handled")
    finally:
        log.append("closed")


log = []
gen = logger(log)
next(gen)
gen.send("a")
gen.throw(ValueError)
gen.send("b")
gen.close()
print("log:", log)
print("state:", inspect.getgeneratorstate(gen))


# 3
def inner():
    yield "step"
    return "inner result"


def outer():
    result = yield from inner()
    yield f"outer got {result!r}"


print(list(outer()))
