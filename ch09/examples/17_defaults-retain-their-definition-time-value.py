shipping = 5

def delivered_total(price, delivery=shipping):
    return price + delivery

shipping = 9
print(delivered_total(20))
print(delivered_total(20, shipping))
