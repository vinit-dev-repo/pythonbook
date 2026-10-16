class SwallowErrors:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"quietly ignoring: {exc_value}")
        return True             # True = "I handled it, do not re-raise"

with SwallowErrors():
    print("before the crash")
    1 / 0
    print("this line never runs")

print("the program is still running!")
