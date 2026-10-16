class PositiveNumber:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("must be positive")
        self.value = value

class Product:
    price = PositiveNumber()

    def __init__(self, price):
        self.price = price

p = Product(9.99)
print(p.price)
