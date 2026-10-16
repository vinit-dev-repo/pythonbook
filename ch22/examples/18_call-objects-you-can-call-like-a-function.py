class CallCounter:
    def __init__(self):
        self.count = 0

    def __call__(self, *args):
        self.count += 1
        print(f"Called {self.count} time(s) with {args}")

counter = CallCounter()
counter(1, 2)
counter("hello")
print(callable(counter))
