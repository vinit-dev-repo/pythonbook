# package_api/check.py
import myapp
from myapp import shout_number
from myapp.utils.numbers import shout_number as implementation

print(myapp.shout_number(42))
print(shout_number is implementation)
print(myapp.__all__)
