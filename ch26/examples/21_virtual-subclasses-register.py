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

    def receipt(self, amount):
        return f"local receipt: {amount}"


class ReceiptAdapter(ReceiptGateway):
    def __init__(self, gateway):
        self._gateway = gateway

    def charge(self, amount):
        return self._gateway.charge(amount)


ReceiptGateway.register(OldGateway)
print(OldGateway().receipt(9))
print(ReceiptAdapter(OldGateway()).receipt(9))
