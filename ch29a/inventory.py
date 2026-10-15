# inventory.py
from counted import CountedCalls

def make_inventory(decorator_type=CountedCalls):
    class Inventory:
        def __init__(self, name, quantity):
            self.name = name
            self.quantity = quantity
            self._call_counts = {}

        @decorator_type
        def add(self, amount, *, reason='stock'):
            """Add a positive built-in integer and return the named result."""
            if type(amount) is not int or amount <= 0:
                raise ValueError('amount must be a positive built-in int')
            self.quantity += amount
            return f'{self.name}:{self.quantity}:{reason}'

        @decorator_type
        def quantity_now(self):
            """Return this inventory quantity without changing it."""
            return self.quantity
    return Inventory

Inventory = make_inventory()

def format_stock(name, *, width=0):
    return f'{name:>{width}}'
