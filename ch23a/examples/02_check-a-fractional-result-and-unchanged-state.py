from person import Person

sam = Person("Sam Reed", pay=100)
sam.giveRaise(0.015)
print(sam.pay)

limit = Person("Limit Case", pay=10**12)
try:
    limit.giveRaise(0.10)
except ValueError as error:
    print(error)
print(limit.pay)
