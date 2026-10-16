try:
    prices = {"milk": 1.50}
    print(prices["bread"])
except KeyError as e:
    print(f"Missing key: {e}")
