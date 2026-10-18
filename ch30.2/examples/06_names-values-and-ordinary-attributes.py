from enum import Enum

class Delivery(Enum):
    LOCAL = 10
    REMOTE = 20

Delivery.LOCAL._add_alias_('NEARBY')
Delivery.LOCAL._add_value_alias_(99)
print(Delivery['NEARBY'] is Delivery.LOCAL)
print(Delivery(99) is Delivery.LOCAL)
print(Delivery.NEARBY.name, Delivery.NEARBY.value)
print(len(Delivery), list(Delivery.__members__))
