# risky — catches and hides everything, even typos in your own code
try:
    result = 10 / 0
except:
    print("something went wrong")

# Pythonic — name the exception you actually expect
try:
    result = 10 / 0
except ZeroDivisionError:
    print("cannot divide by zero")
