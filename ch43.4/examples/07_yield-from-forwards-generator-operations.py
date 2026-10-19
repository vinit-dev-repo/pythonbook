def inner():
    try:
        while True:
            try:
                received = yield
                print("inner got:", received)
            except ValueError as e:
                print("inner caught:", e)
    finally:
        print("inner closing")

def outer():
    yield from inner()   # a two-way pipe, not just a one-way flatten

gen = outer()
next(gen)
gen.send("hello")               # forwarded down to inner
gen.throw(ValueError("oops"))   # forwarded down to inner too -- inner survives
gen.close()                     # forwarded down to inner too -- runs inner's finally
