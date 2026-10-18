# 1
from decimal import Decimal
total = Decimal("2.10") + Decimal("3.45")
print(total.quantize(Decimal("0.01")))   # 5.55

# 2
import statistics
data = [2, 2, 6, 6]
print(statistics.mean(data))     # 4
print(statistics.median(data))   # 4.0
print(statistics.mode(data))     # 2
try:
    statistics.stdev([2])
except statistics.StatisticsError as error:
    print("StatisticsError:", error)

# 3
from decimal import Decimal
print(Decimal(0.1))     # 0.1000000000000000055511151231257827021181583404541015625
print(Decimal("0.1"))   # 0.1
