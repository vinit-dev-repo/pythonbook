def get_price(catalogue, item_name):
    return catalogue[item_name]

def checkout(catalogue):
    return get_price(catalogue, "bread")

prices = {"milk": 1.50, "eggs": 2.00}
checkout(prices)
