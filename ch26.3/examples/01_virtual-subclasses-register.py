import abc

class PaymentGateway(abc.ABC):
    @abc.abstractmethod
    def charge(self, amount):
        """Charge the given amount. Return a transaction id."""

    @abc.abstractmethod
    def refund(self, transaction_id):
        """Refund a previous charge."""

    def describe(self):
        return f"{type(self).__name__} payment gateway"

class LegacyGateway:
    """Comes from a third-party library - we cannot edit its source."""
    def charge(self, amount):
        return f"legacy-txn-{amount}"

    def refund(self, transaction_id):
        return f"legacy-refund {transaction_id}"

print(isinstance(LegacyGateway(), PaymentGateway))
PaymentGateway.register(LegacyGateway)
print(isinstance(LegacyGateway(), PaymentGateway))
print(issubclass(LegacyGateway, PaymentGateway))
print(LegacyGateway.__mro__)
