import abc


class Delivery(abc.ABC):
    @abc.abstractmethod
    def send(self, message):
        pass


class BrokenDelivery:
    pass


Delivery.register(BrokenDelivery)
print(isinstance(BrokenDelivery(), Delivery))
try:
    BrokenDelivery().send("hello")
except AttributeError as error:
    print(type(error).__name__)
