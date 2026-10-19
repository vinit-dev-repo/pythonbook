def logger():
    try:
        while True:
            msg = yield
            print("log:", msg)
    finally:
        print("logger shutting down")

gen = logger()
next(gen)
gen.send("first entry")
gen.close()             # injects GeneratorExit -- runs the finally, then stops
