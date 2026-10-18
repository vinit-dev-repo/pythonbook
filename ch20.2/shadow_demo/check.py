# shadow_demo/check.py
import random

try:
    print(random.randint(1, 10))
except AttributeError:
    print("local random.py has no randint")
