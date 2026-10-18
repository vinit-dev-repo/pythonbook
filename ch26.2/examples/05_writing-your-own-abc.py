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

try:
    gateway = PaymentGateway()
except TypeError as e:
    print("TypeError:", e)
