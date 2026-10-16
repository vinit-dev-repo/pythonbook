with Timer() as t:
    time.sleep(0.5)               # stand in for some slow work
    total = sum(range(1_000_000))

print("done:", total)
