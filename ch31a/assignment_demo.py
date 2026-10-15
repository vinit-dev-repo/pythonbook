# assignment_demo.py
from fields import IntegerField


class Record:
    seats = IntegerField(0, 2)


if __name__ == "__main__":
    first = Record()
    first.seats = 0
    try:
        first.seats = 3
    except ValueError as error:
        print(error)
    print(first.seats)
    first.seats = 1
    print(first.seats)
    unset = Record()
    try:
        unset.seats = 3
    except ValueError:
        pass
    print("_seats" in unset.__dict__)
