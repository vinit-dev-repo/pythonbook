# ticket_transfer.py
from counted import CountedCalls

class TicketOffice:
    def __init__(self, tickets):
        self.tickets = tickets
        self._call_counts = {}

    @CountedCalls
    def sell(self, amount):
        if type(amount) is not int or amount <= 0 or amount > self.tickets:
            raise ValueError('sale refused')
        self.tickets -= amount
        return self.tickets

    @CountedCalls
    def remaining(self):
        return self.tickets

if __name__ == '__main__':
    first = TicketOffice(5)
    second = TicketOffice(4)
    saved = first.sell
    print(saved(2), second.remaining())
    try:
        first.sell(9)
    except ValueError:
        print(first.tickets)
    second.saved = saved
    print(second.saved(1), first.tickets, second.tickets)
    sell = vars(TicketOffice)['sell']
    remaining = vars(TicketOffice)['remaining']
    print(
        sell.calls_for(first), sell.calls_for(second), sell.total_calls,
        remaining.calls_for(first), remaining.calls_for(second),
        remaining.total_calls,
    )
