for level in (19, 20, 25, 30, 31):
    try:
        print("Accepted:", validate_level(level))
    except RangeError as error:
        print("Rejected:", error.value, "bounds:", error.lower, error.upper)

try:
    validate_level(True)
except TypeError:
    print("Boolean rejected as the wrong type")
