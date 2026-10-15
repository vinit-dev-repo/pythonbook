# schedule_search.py
from bisect import bisect_right

bookings = [(8, 10, "review"), (12, 15, "workshop"), (18, 20, "cleanup")]

def booking_at(slot):
    index = bisect_right(bookings, slot, key=lambda row: row[0]) - 1
    if index >= 0 and slot < bookings[index][1]:
        return bookings[index][2]
    return "free"

for slot in (7, 8, 9, 10, 11, 12, 19, 20):
    print(slot, booking_at(slot))
