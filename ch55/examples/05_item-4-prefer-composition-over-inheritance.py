# Inheritance — Car IS-A Engine? That's not really true.
class Engine:
    def start(self):
        print("Engine starting")

class Car(Engine):
    def drive(self):
        self.start()
        print("Driving")

# Composition — Car HAS-A Engine. True to real life.
class Car2:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        self.engine.start()
        print("Driving")

Car2(Engine()).drive()
