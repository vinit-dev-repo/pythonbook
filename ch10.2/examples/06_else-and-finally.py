def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(f"Success: {result}")
    finally:
        print("Division attempt finished")

divide(10, 2)
print("---")
divide(10, 0)
