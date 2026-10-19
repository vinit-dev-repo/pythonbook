# exercise_lock_order.py
from lock_order import opposite_order, same_order

outcomes = opposite_order()
assert len(outcomes) == 2
assert all(value in {"completed", "timed out"} for value in outcomes)
assert outcomes.count("timed out") >= 1
assert same_order() == ["completed", "completed"]
print("lock-order assertions passed")
