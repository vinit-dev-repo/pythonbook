class PositiveNumber:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name   # e.g. "_price"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.private_name]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("must be positive")
        instance.__dict__[self.private_name] = value

class Product:
    price = PositiveNumber()
    quantity = PositiveNumber()

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

apple = Product(1.50, 100)
banana = Product(0.60, 250)

print(apple.price, apple.quantity)
print(banana.price, banana.quantity)
print(apple.__dict__)
