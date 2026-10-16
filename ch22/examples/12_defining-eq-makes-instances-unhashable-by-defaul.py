m = Money(50)
wallet = {m}
print(m in wallet)
m.amount = 99            # the hash was built from amount - now it is stale
print(m in wallet)       # still in the set, but unfindable
print(len(wallet))
