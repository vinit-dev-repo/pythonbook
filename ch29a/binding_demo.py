# binding_demo.py
from counted import CountedCalls
from inventory import Inventory, format_stock

if __name__ == '__main__':
    format_call = CountedCalls(format_stock)
    east, west = Inventory('east', 10), Inventory('west', 20)
    first, second = east.add, east.add
    raw = vars(Inventory)['add']
    print(
        first is second, first.subject is east, first.decorator is raw,
        raw.calls_for(east), raw.total_calls,
    )
    print(
        first(2), west.add(3), second(4, reason='delivery'),
        Inventory.add(east, 1, reason='audit'),
    )
    try:
        east.add(-1)
    except ValueError as error:
        print(type(error).__name__)
    print(
        east.quantity, west.quantity,
        raw.calls_for(east), raw.calls_for(west), raw.total_calls,
    )
    west.saved = first
    print(west.saved(1))
    print(
        east.quantity, west.quantity,
        raw.calls_for(east), raw.calls_for(west), raw.total_calls,
    )
    print(format_call('east', width=6), format_call.total_calls)
    try:
        format_call()
    except TypeError as error:
        print(type(error).__name__, format_call.total_calls)
