# nested_record.py
readings = [("north", (12, 18)), ("south", (15, 16))]
for station, (low, high) in readings:
    print(station, high - low)

station = "before"
low = high = -1
try:
    station, (low, high) = ("broken", (9,))
except ValueError:
    print("inner pair missing a value")
print(station, low, high)
