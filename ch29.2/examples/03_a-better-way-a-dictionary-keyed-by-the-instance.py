class PositiveNumber:
    def __init__(self):
        self.data = {}   # instance -> value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data[instance]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("must be positive")
        self.data[instance] = value

class Product:
    price = PositiveNumber()

    def __init__(self, price):
        self.price = price

apple = Product(1.50)
banana = Product(0.60)
print(apple.price)
print(banana.price)
