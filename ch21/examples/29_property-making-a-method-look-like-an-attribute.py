try:
    acc.balance = 200
except AttributeError as error:
    print(type(error).__name__)
print(acc.balance)
