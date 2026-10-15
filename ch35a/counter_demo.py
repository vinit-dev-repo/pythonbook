# counter_demo.py
from itertools import count


class LastUsedCounter:
    def __init__(self, last_used):
        self.last_used = last_used

    def __iter__(self):
        return self

    def __next__(self):
        self.last_used += 1
        return self.last_used


def after(last_used):
    while True:
        last_used += 1
        yield last_used


if __name__ == '__main__':
    for label, source in [('iterator', LastUsedCounter(100)),
                          ('generator', after(100)), ('count', count(100))]:
        values = [next(source) for _ in range(3)]
        print(label + ':', values)
