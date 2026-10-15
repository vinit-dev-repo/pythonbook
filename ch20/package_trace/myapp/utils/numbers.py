# package_trace/myapp/utils/numbers.py
print("initializing myapp.utils.numbers")
from . import strings

def shout_number(n):
    return strings.shout(str(n))
