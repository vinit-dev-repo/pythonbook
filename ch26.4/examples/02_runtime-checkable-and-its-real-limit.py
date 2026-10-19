from typing import Protocol, runtime_checkable


@runtime_checkable
class SupportsCharge(Protocol):
    def charge(self, amount: float) -> str: ...
    def refund(self, transaction_id: str) -> str: ...


class WrongShapeGateway:
    """Has methods NAMED right, but the wrong signature."""
    def charge(self):          # missing the 'amount' parameter
        return "wrong-shape-txn"

    def refund(self, transaction_id):
        return f"wrong-shape-refund {transaction_id}"


wsg = WrongShapeGateway()
print(isinstance(wsg, SupportsCharge))   # shallow runtime member check

try:
    wsg.charge(50)
except TypeError as e:
    print("Failed at call time:", e)
