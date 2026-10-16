try:
    total = compute_order_total(order)
except Exception:
    total = 0   # WRONG: hides every possible bug and gives a fake answer
