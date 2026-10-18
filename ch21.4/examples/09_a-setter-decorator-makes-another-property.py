class Gauge:
    def __init__(self, level):
        self._level = level

    @property
    def level(self):
        """The stored level."""
        return self._level

    @level.setter
    def writable_level(self, value):
        """Assign a level."""
        self._level = value

gauge = Gauge(10)
print(Gauge.level is Gauge.writable_level)
print(Gauge.level.fget is Gauge.writable_level.fget)
print(Gauge.level.fset is None)
print(Gauge.writable_level.fset is None)
try:
    gauge.level = 20
except AttributeError as error:
    print(type(error).__name__)
gauge.writable_level = 20
print(gauge.level, gauge.writable_level)
print(Gauge.writable_level.__doc__)
