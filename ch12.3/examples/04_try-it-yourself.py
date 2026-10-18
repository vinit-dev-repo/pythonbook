# 1
import math
print(math.floor(-2.5))   # -3
print(math.ceil(-2.5))    # -2

# 2
import math
best = math.inf
for number in [7, 3, 9]:
    if number < best:
        best = number
print(best)               # 3

# 3
import bisect
scores = [10, 20, 30, 40, 50]
print(bisect.bisect_left(scores, 30))    # 2
print(bisect.bisect_right(scores, 30))   # 3
bisect.insort(scores, 35)
print(scores)                            # [10, 20, 30, 35, 40, 50]

# 4
from collections import deque
recent = deque(maxlen=3)
for number in range(1, 6):
    recent.append(number)
print(list(recent))       # [3, 4, 5]
recent.rotate(1)
print(list(recent))       # [5, 3, 4]

# 5
from array import array
readings = array("d", [1.5, 2.5])
rebuilt = array("d")
rebuilt.frombytes(readings.tobytes())
print(rebuilt == readings)   # True
