# 1
class Device:
    def setup(self):
        return ["device"]

class Printer(Device):
    def setup(self):
        return Device.setup(self) + ["printer"]

class Scanner(Device):
    def setup(self):
        return Device.setup(self) + ["scanner"]

class AllInOne(Printer, Scanner):
    def setup(self):
        return Printer.setup(self) + Scanner.setup(self)

print(AllInOne().setup())  # ['device', 'printer', 'device', 'scanner']

# 2
class Device2:
    def setup(self):
        return ["device"]

class Printer2(Device2):
    def setup(self):
        return super().setup() + ["printer"]

class Scanner2(Device2):
    def setup(self):
        return super().setup() + ["scanner"]

class AllInOne2(Printer2, Scanner2):
    def setup(self):
        return super().setup() + ["all-in-one"]

print(AllInOne2().setup())  # ['device', 'scanner', 'printer', 'all-in-one']

# 3
print([cls.__name__ for cls in AllInOne2.__mro__])
# ['AllInOne2', 'Printer2', 'Scanner2', 'Device2', 'object']
