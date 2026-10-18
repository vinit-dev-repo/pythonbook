class Device2:
    def setup(self):
        print("Device ready")

class Printer2(Device2):
    def setup(self):
        print("Printer ready")
        super().setup()             # "whoever is next in line", not a named parent

class Scanner2(Device2):
    def setup(self):
        print("Scanner ready")
        super().setup()

class AllInOne2(Printer2, Scanner2):
    def setup(self):
        print("AllInOne ready")
        super().setup()

AllInOne2().setup()
