prices = [40, 10, 30, 20]

new_list = sorted(prices)     # prices is untouched
print(new_list)
print(prices)

prices.sort()                  # prices itself is now sorted
print(prices)
