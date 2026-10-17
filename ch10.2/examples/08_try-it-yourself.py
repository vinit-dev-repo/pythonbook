# 1
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # None

# 2
try:
    n = int(input("Enter a number: "))
    print(f"You entered {n}")
except ValueError:
    print("Please enter digits only")

# 3
for value in ["10", "0", "x", "5"]:
    try:
        print(100 / int(value))
    except ValueError:
        print(f"{value!r} is not a number")
    except ZeroDivisionError:
        print("Cannot divide by zero")

# 4
try:
    print("trying")
    x = 5 / 1
except ZeroDivisionError:
    print("caught")
else:
    print("else ran, result:", x)
finally:
    print("finally always runs")
# trying
# else ran, result: 5.0
# finally always runs
