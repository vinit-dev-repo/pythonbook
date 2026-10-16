from collections import namedtuple

Stock = namedtuple("Stock", "code quantity")
incoming = {"quantity": 6, "code": "P-17"}
stock = Stock(**incoming)
revised = stock._replace(quantity=8)
print(stock)
print(revised)
print(incoming)
print(stock._asdict())
