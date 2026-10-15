# recent_events.py
from collections import deque

recent = deque(["start", "load", "edit"], maxlen=3)
recent.append("save")
print(list(recent))
recent.rotate(1)
print(list(recent))
recent.rotate(-1)
recent.extendleft(["retry", "check"])
print(list(recent))
before = list(recent)
try:
    recent.insert(1, "extra")
except IndexError:
    print("full insert rejected:", list(recent) == before)
