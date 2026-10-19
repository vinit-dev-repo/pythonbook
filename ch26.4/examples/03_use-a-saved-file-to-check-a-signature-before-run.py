from typing import Protocol


class ChargePort(Protocol):
    def charge(self, amount: float) -> str: ...
    def refund(self, transaction_id: str) -> str: ...


def settle(port: ChargePort) -> str:
    return port.charge(12.5)


class StoreCredit:
    def charge(self, amount: float) -> str:
        return f"credit-{amount}"

    def refund(self, transaction_id: str) -> str:
        return f"refund-{transaction_id}"


class WrongCharge:
    def charge(self) -> str:
        return "wrong"

    def refund(self, transaction_id: str) -> str:
        return f"refund-{transaction_id}"


print(settle(StoreCredit()))
try:
    print(settle(WrongCharge()))
except TypeError as error:
    print("Failed at call time:", error)
