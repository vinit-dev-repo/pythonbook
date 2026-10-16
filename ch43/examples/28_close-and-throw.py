def resilient_logger():
    while True:
        try:
            msg = yield
            print("log:", msg)
        except ValueError as e:
            print("logger caught and handled:", e)

gen = resilient_logger()
next(gen)
gen.send("first entry")
gen.throw(ValueError("bad entry"))   # injects the exception AT the paused yield
gen.send("still alive")
