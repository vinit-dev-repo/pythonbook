# ticket_transfer.py
from bingo import BingoCage
from lotto import LotteryBlower
from tombolist import TomboList


def draw_tickets(device, batch):
    device.load(batch)
    before_draw = device.inspect()
    drawn = []
    while True:
        try:
            drawn.append(device.pick())
        except LookupError:
            break
    result = tuple(sorted(drawn))
    assert result == before_draw
    assert device.loaded() is False
    return before_draw, result


if __name__ == '__main__':
    for implementation in (BingoCage, LotteryBlower, TomboList):
        device = implementation([2, 1])
        batch = (ticket for ticket in (2, 3))
        before_draw, drawn = draw_tickets(device, batch)
        assert before_draw == (1, 2, 2, 3)
        print(implementation.__name__, 'snapshot:', before_draw,
              'draws:', drawn, 'loaded after draw:', device.loaded())
