def sub():
    yield "working..."
    yield "still working..."
    return "sub finished with this result"

def outer():
    x = yield from sub()          # x captures sub()'s RETURN value, not a yielded one
    yield f"outer received: {x!r}"

gen = outer()
for value in gen:
    print(value)
