# cast_buffer.py
from array import array
import sys

numbers = array("I", [0, 0])
view = memoryview(numbers)
octets = view.cast("B")
offset = 0 if sys.byteorder == "little" else numbers.itemsize - 1
octets[offset] = 9
print(numbers.tolist())
readonly = view.toreadonly()
numbers[1] = 7
print("readonly sees changes:", readonly.tolist())
try:
    readonly[0] = 3
except TypeError:
    print("write through readonly rejected")
try:
    numbers.append(8)
except BufferError:
    print("resize while exported rejected")
readonly.release()
octets.release()
view.release()
numbers.append(8)
print("after release:", numbers.tolist())
