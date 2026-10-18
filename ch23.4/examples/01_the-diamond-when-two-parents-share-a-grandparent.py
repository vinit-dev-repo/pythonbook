class Device:
    def setup(self):
        print("Device ready")

class Printer(Device):
    def setup(self):
        print("Printer ready")
        Device.setup(self)          # naming the parent directly

class Scanner(Device):
    def setup(self):
        print("Scanner ready")
        Device.setup(self)          # naming the parent directly

class AllInOne(Printer, Scanner):
    def setup(self):
        print("AllInOne ready")
        Printer.setup(self)
        Scanner.setup(self)

AllInOne().setup()
