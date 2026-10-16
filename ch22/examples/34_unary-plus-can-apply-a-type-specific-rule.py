from collections import Counter

stock = Counter(ready=4, held=0, shortage=-2)
print(dict(+stock))
print(dict(-stock))
print(dict(stock))
