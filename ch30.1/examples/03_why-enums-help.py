from enum import Enum

class OrderStatus(Enum):
    PLACED = 1
    PAID = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELLED = 5

status = OrderStatus.PAID
print(status)
