# myapp/utils/numbers.py
from . import strings   # "from THIS package" (myapp.utils)

def shout_number(n):
    return strings.shout(str(n))
