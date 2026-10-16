from typing import Protocol, runtime_checkable


@runtime_checkable
class SupportsCharge(Protocol):
    def charge(self, amount: float) -> str: ...
    def refund(self, transaction_id: str) -> str: ...


class WalletApp:
    """Never heard of PaymentGateway - no inheritance, no registration."""
    def charge(self, amount):
        return f"wallet-txn-{amount}"

    def refund(self, transaction_id):
        return f"wallet-refund {transaction_id}"


class StripeGateway:
    def charge(self, amount):
        return f"stripe-txn-{amount}"

    def refund(self, transaction_id):
        return f"refunded {transaction_id}"


print(isinstance(WalletApp(), SupportsCharge))
print(isinstance(StripeGateway(), SupportsCharge))
print(isinstance(42, SupportsCharge))
