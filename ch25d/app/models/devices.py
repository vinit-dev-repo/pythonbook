# app/models/devices.py
from app.models.resource import Resource
from app.utils.validators import validate_integer, validate_text


class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated, cores, socket, power_watts):
        super().__init__(name, manufacturer, total, allocated)
        validate_integer("cores", cores, min_value=1)
        self._cores = cores
        self._socket = validate_text("socket", socket)
        validate_integer("power_watts", power_watts, min_value=1)
        self._power_watts = power_watts

    @property
    def cores(self):
        return self._cores
    @property
    def socket(self):
        return self._socket
    @property
    def power_watts(self):
        return self._power_watts

    def __repr__(self):
        return f"CPU(category={self.category!r}, name={self.name!r}, socket={self.socket!r}, cores={self.cores!r})"


class Storage(Resource):
    def __init__(self, name, manufacturer, total, allocated, capacity_gb):
        super().__init__(name, manufacturer, total, allocated)
        validate_integer("capacity_gb", capacity_gb, min_value=1)
        self._capacity_gb = capacity_gb

    @property
    def capacity_gb(self):
        return self._capacity_gb

    def __repr__(self):
        return f"Storage(category={self.category!r}, name={self.name!r}, capacity_gb={self.capacity_gb!r})"


class HDD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_gb, size, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_gb)
        if type(size) is not str:
            raise TypeError("size must be a string")
        if size not in ('2.5\"', '3.5\"'):
            raise ValueError('size must be 2.5\" or 3.5\"')
        self._size = size
        validate_integer("rpm", rpm, min_value=1000, max_value=50000)
        self._rpm = rpm

    @property
    def size(self):
        return self._size
    @property
    def rpm(self):
        return self._rpm

    def __repr__(self):
        return f"{super().__repr__()[:-1]}, size={self.size!r}, rpm={self.rpm!r})"


class SSD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_gb, interface):
        super().__init__(name, manufacturer, total, allocated, capacity_gb)
        self._interface = validate_text("interface", interface)

    @property
    def interface(self):
        return self._interface

    def __repr__(self):
        return f"{super().__repr__()[:-1]}, interface={self.interface!r})"
