@timer
def slow_add(a, b):
    time.sleep(0.1)
    return a + b

slow_add(2, 3)
