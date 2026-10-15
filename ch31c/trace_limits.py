# trace_limits.py
from tracer_lab import Tracer


@Tracer
class Bag(list):
    pass


if __name__ == '__main__':
    bag = Bag(['a'])
    bag.append('b')
    print(bag.__len__())
    try:
        len(bag)
    except TypeError as error:
        print(type(error).__name__)
    print(isinstance(bag, Bag), isinstance(bag, list), isinstance(bag._target, list), bag.lookups)
