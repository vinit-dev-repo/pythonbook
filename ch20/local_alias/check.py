# local_alias/check.py
import sys
import loud as first
import loud as second
print(first is second, first.__name__, "loud" in globals())

def read_value():
    import loud
    return loud.value

print(read_value(), read_value())
print("loud" in globals(), first is sys.modules["loud"])
first = "a different caller value"
print(second.value)
