# booking_transfer.py
from fields import CharField, IntegerField

class Booking:
    seats = IntegerField(1, 4)
    table = IntegerField(1, 4)
    label = CharField(1, 3)
    note = IntegerField()

if __name__ == "__main__":
    first, second = Booking(), Booking()
    first.seats, first.table, first.label, first.note = 1, 4, "é", 10**80
    second.seats = 4
    try:
        first.seats = 5
    except ValueError as error:
        print(error)
    print(first.seats, first.table, first.label, second.seats)
    print(first.note)
