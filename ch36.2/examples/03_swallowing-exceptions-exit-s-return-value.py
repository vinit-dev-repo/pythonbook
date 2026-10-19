class LogButDontSwallow:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"logged: {exc_value}")
        return False            # False = "let it keep going"

with LogButDontSwallow():
    1 / 0
