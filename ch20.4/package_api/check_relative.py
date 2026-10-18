# package_api/check_relative.py
import importlib
import myapp.utils.numbers

found = importlib.import_module(".numbers", package="myapp.utils")
print(found is myapp.utils.numbers)
print(found.shout_number(7))
