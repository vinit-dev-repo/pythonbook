from enum import Enum, StrEnum, auto
import json

# 1 and 2
class TrafficLight(Enum):
    RED = auto()
    GREEN = auto()
    YELLOW = auto()

    def next_light(self):
        order = [TrafficLight.RED, TrafficLight.GREEN, TrafficLight.YELLOW]
        return order[(order.index(self) + 1) % len(order)]

print(TrafficLight.RED.next_light())       # TrafficLight.GREEN

# 3
print(TrafficLight["GREEN"])   # TrafficLight.GREEN
print(TrafficLight(1))          # TrafficLight.RED

# 4
class Weekday(StrEnum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"

print(json.dumps({"day": Weekday.MONDAY}))   # {"day": "monday"}
