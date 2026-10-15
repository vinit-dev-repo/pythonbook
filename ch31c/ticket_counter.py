# ticket_counter.py
from attribute_policy import Public


class TicketCounter:
    def __init__(self, count):
        self.count = count

    def advance(self, amount):
        if type(amount) is not int or amount <= 0:
            raise ValueError('amount must be a positive exact int')
        self.count += amount
        return self.count

    def report(self):
        return f'tickets={self.count}'


if __name__ == '__main__':
    Counter = Public('advance', 'report')(TicketCounter)
    left = Counter(1)
    right = Counter(10)
    print(left.advance(2), right.report())
    try:
        left.count = 99
    except TypeError as error:
        print(type(error).__name__, left.report())
    try:
        left.advance(0)
    except ValueError as error:
        print(type(error).__name__, left.report(), right.report())
