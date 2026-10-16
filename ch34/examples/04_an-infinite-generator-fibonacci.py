def fibonacci():
    a, b = 0, 1
    while True:            # never stops on its own
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(8):
    print(next(fib), end=" ")
