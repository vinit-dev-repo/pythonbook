from collections import defaultdict

stock = defaultdict(int)
print(stock.get("slot"), list(stock))
print(stock["slot"], list(stock))

def unavailable():
    raise ValueError("no starting value")

pending = defaultdict(unavailable)
try:
    pending["slot"]
except ValueError as error:
    print(error)
print(list(pending))
