for raw in ("paid", "shpped"):
    try:
        status = OrderStatus(raw)
    except ValueError:
        print("unknown status:", raw)
    else:
        print(next_step(status))
try:
    next_step("paid")
except TypeError as error:
    print(type(error).__name__ + ":", error)
