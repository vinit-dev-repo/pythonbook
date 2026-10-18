try:
    acc.interest_earned = 100
except AttributeError as error:
    print(type(error).__name__)
print(acc.interest_earned)
