with timer():
    time.sleep(0.5)               # the same stand-in for slow work as before
    total = sum(range(1_000_000))

print("done:", total)
