# myapp/main.py
from .utils import numbers   # "from the utils sub-package of THIS package"

print(numbers.shout_number(42))
