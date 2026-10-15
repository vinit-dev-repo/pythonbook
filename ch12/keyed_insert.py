# keyed_insert.py
from bisect import bisect_left, bisect_right, insort_right

events = [(4, "open"), (9, "read"), (9, "write"), (15, "close")]
by_slot = lambda event: event[0]
insort_right(events, (9, "check"), key=by_slot)
first = bisect_left(events, 9, key=by_slot)
last = bisect_right(events, 9, key=by_slot)
print(events[first:last])
print(bisect_left(events, 9, lo=2, hi=last, key=by_slot))
