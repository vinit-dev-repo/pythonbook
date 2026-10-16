import math
import itertools

orders = itertools.permutations(range(12))
print("possible orders:", math.factorial(12))
print("first length:", len(next(orders)))
print("second tail:", next(orders)[-3:])
print("empty order:", list(itertools.permutations([])))
