def make_registrar():
    def register(label):
        register.accepted += 1
        return label.upper()
    register.accepted = 0
    return register

morning = make_registrar()
evening = make_registrar()
print(morning("k7"), morning("m2"), evening("p5"))
print(morning.accepted, evening.accepted)
evening.accepted = 10
print(evening("q4"), evening.accepted)
