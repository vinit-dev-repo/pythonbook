import dis

def add_tax(price, rate):
    total = price + price * rate
    return total

dis.dis(add_tax)
