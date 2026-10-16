try:
    result = 10 / 0
    print("You will not see this")
except ZeroDivisionError:
    print("You can't divide by zero!")

print("The program keeps going")
