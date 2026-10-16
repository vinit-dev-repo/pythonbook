class Countdown:
    def __init__(self, start):
        self._start = start

    def __iter__(self):
        n = self._start
        while n > 0:
            yield n            # this method is itself a generator function
            n -= 1

cd = Countdown(3)

for n in cd:
    print("first loop:", n)
for n in cd:                    # works again -- __iter__ is called fresh each time
    print("second loop:", n)
