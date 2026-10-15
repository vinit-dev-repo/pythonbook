# field_demo.py
from fields import CharField, IntegerField


class Record:
    seats = IntegerField(0, 2)
    label = CharField(1, 2)


if __name__ == "__main__":
    first, second = Record(), Record()
    first.seats, second.seats = 0, 2
    first.label, second.label = "é", "e\u0301"
    print(first.seats, second.seats)
    print(len(first.label), len(second.label))
    print(Record.seats.name, Record.seats.storage_name)
