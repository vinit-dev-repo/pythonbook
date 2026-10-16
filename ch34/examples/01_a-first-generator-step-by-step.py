def talkative():
    print("starting")
    yield 1
    print("woke up, about to yield 2")
    yield 2
    print("woke up, about to yield 3")
    yield 3
    print("all done")

gen = talkative()
print("generator created -- nothing has printed yet!")

print(next(gen))
print(next(gen))
print(next(gen))
