def echo():
    while True:
        received = yield          # pauses here, waiting to receive something
        print("got:", received)

gen = echo()
next(gen)              # must "prime" it first -- see below
gen.send("hello")
gen.send("world")
