from enum import Enum

class OrderStatus(Enum):
    PLACED = "placed"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"

def ship_order(status):
    if status == OrderStatus.SHPPED:   # AttributeError when this line runs
        print("Sending tracking email...")
    else:
        print("Not shipped yet")

try:
    ship_order(OrderStatus.SHIPPED)
except AttributeError as e:
    print("Crashed immediately:", e)
