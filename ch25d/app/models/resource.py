# app/models/resource.py
from app.utils.validators import validate_integer, validate_text


class Resource:
    def __init__(self, name, manufacturer, total, allocated):
        self._name = validate_text("name", name)
        self._manufacturer = validate_text("manufacturer", manufacturer)
        validate_integer("total", total, min_value=0)
        validate_integer("allocated", allocated, min_value=0, max_value=total)
        self._total = total
        self._allocated = allocated

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    @property
    def available(self):
        return self.total - self.allocated

    @property
    def category(self):
        return type(self).__name__.lower()

    def __str__(self):
        return self.name

    def __repr__(self):
        return (
            f"Resource(name={self.name!r}, category={self.category!r}, "
            f"manufacturer={self.manufacturer!r}, total={self.total!r}, "
            f"allocated={self.allocated!r})"
        )

    def _amount(self, amount):
        validate_integer("amount", amount, min_value=1)

    def claim(self, amount):
        self._amount(amount)
        next_allocated = self.allocated + amount
        if next_allocated > self.total:
            raise ValueError("cannot claim more than available resources")
        self._allocated = next_allocated

    def freeup(self, amount):
        self._amount(amount)
        next_allocated = self.allocated - amount
        if next_allocated < 0:
            raise ValueError("cannot free more than allocated resources")
        self._allocated = next_allocated

    def died(self, amount):
        self._amount(amount)
        next_total = self.total - amount
        next_allocated = self.allocated - amount
        if next_allocated < 0:
            raise ValueError("cannot retire more than allocated resources")
        self._total = next_total
        self._allocated = next_allocated

    def purchased(self, amount):
        self._amount(amount)
        next_total = self.total + amount
        self._total = next_total
