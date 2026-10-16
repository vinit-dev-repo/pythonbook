def divide_hundred_by(text):
    return 100 / int(text)

for value in ["10", "0", "abc"]:
    try:
        print(divide_hundred_by(value))
    except (ValueError, ZeroDivisionError):
        print(f"Could not process {value!r}")
