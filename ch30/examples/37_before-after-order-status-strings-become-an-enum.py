def ship_order(status):
    if status == OrderStatus.SHIPPED:
        print("Sending tracking email...")
    else:
        print("Not shipped yet")

ship_order(OrderStatus.SHIPPED)
