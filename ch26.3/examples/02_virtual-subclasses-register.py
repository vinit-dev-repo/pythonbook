import abc

class ReceiptGateway(abc.ABC):
    @abc.abstractmethod
    def charge(self, amount):
        pass

    def receipt(self, amount):
        return f"receipt: {self.charge(amount)}"

class OldGateway:
    def charge(self, amount):
        return f"old-{amount}"

ReceiptGateway.register(OldGateway)
try:
    OldGateway().receipt(5)
except AttributeError as error:
    print(type(error).__name__)

class ReceiptAdapter(ReceiptGateway):
    def __init__(self, gateway):
        self._gateway = gateway

    def charge(self, amount):
        return self._gateway.charge(amount)

print(ReceiptAdapter(OldGateway()).receipt(5))
