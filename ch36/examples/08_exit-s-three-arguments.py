class Inspector:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print("exited cleanly, no error")
        else:
            print(f"exited because of: {exc_type.__name__}: {exc_value}")

with Inspector():
    print("no problems here")

with Inspector():
    print("about to explode")
    1 / 0
