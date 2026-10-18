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

class StripeGateway(PaymentGateway):
    def charge(self, amount):
        return f"stripe-txn-{amount}"

    def refund(self, transaction_id):
        return f"refunded {transaction_id}"

class FakeGateway(PaymentGateway):
    """Stands in for Stripe during tests - no network call."""
    def __init__(self):
        self.charges = []

    def charge(self, amount):
        self.charges.append(amount)
        return f"fake-txn-{len(self.charges)}"

    def refund(self, transaction_id):
        return f"pretend-refunded {transaction_id}"

def checkout(gateway, amount):
    txn = gateway.charge(amount)
    print(gateway.describe(), "->", txn)

checkout(StripeGateway(), 42)
checkout(FakeGateway(), 42)
