from enum import Enum

class OrderStatus(Enum):
    PLACED = "placed"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"

def next_step(status):
    if not isinstance(status, OrderStatus):
        raise TypeError("status must be an OrderStatus")
    match status:
        case OrderStatus.PLACED:
            return "Waiting for payment"
        case OrderStatus.PAID:
            return "Preparing for shipping"
        case OrderStatus.SHIPPED:
            return "On the way"
        case OrderStatus.DELIVERED:
            return "All done"
        case _:
            raise ValueError("unhandled order status")

for s in OrderStatus:
    print(s.name, "->", next_step(s))
