# tests/test_devices.py
import pytest

from app.models.devices import CPU, HDD, SSD, Storage
from app.models.resource import Resource


class IntChild(int):
    pass


class StrChild(str):
    pass


CASES = [
    (Resource, {}),
    (CPU, dict(cores=8, socket='AM5', power_watts=65)),
    (Storage, dict(capacity_gb=100)),
    (HDD, dict(capacity_gb=100, size='3.5"', rpm=7200)),
    (SSD, dict(capacity_gb=100, interface='NVMe')),
]


def state(item):
    return item.total, item.allocated, item.available


@pytest.mark.parametrize('cls, extra', CASES)
def test_all_five_classes_share_the_full_stock_trace_and_rejection(cls, extra):
    item = cls(' Device ', ' Acme ', 10, 3, **extra)
    assert (item.name, item.manufacturer, item.category, str(item)) == ('Device', 'Acme', cls.__name__.lower(), 'Device')
    assert state(item) == (10, 3, 7)
    for action, amount, expected in [('claim', 2, (10, 5, 5)), ('freeup', 1, (10, 4, 6)),
                                     ('died', 2, (8, 2, 6)), ('purchased', 4, (12, 2, 10))]:
        assert getattr(item, action)(amount) is None
        assert state(item) == expected
    before = (state(item), vars(item).copy())
    with pytest.raises(ValueError):
        item.claim(11)
    assert (state(item), vars(item)) == before
    for key, expected in extra.items():
        assert getattr(item, key) == expected


def test_device_fields_and_exact_representations():
    cpu = CPU('Xeon', 'Intel', 4, 1, 8, ' LGA ', 95)
    disk = Storage('Disk', 'Seagate', 2, 0, 500)
    hdd = HDD('Archive', 'Seagate', 2, 0, 1000, '3.5"', 7200)
    ssd = SSD('Flash', 'Acme', 2, 0, 512, ' NVMe ')
    assert (cpu.cores, cpu.socket, cpu.power_watts) == (8, 'LGA', 95)
    assert (disk.capacity_gb, hdd.capacity_gb, hdd.size, hdd.rpm) == (500, 1000, '3.5"', 7200)
    assert (ssd.capacity_gb, ssd.interface) == (512, 'NVMe')
    assert repr(cpu) == "CPU(category='cpu', name='Xeon', socket='LGA', cores=8)"
    assert repr(disk) == "Storage(category='storage', name='Disk', capacity_gb=500)"
    assert repr(hdd) == "Storage(category='hdd', name='Archive', capacity_gb=1000, size='3.5\"', rpm=7200)"
    assert repr(ssd) == "Storage(category='ssd', name='Flash', capacity_gb=512, interface='NVMe')"


@pytest.mark.parametrize('cls, extra', CASES[1:])
def test_device_properties_are_read_only(cls, extra):
    item = cls('Device', 'Acme', 10, 3, **extra)
    before = vars(item).copy()
    for field in extra:
        with pytest.raises(AttributeError):
            setattr(item, field, 1)
        with pytest.raises(AttributeError):
            delattr(item, field)
    assert vars(item) == before


INTEGER_FIELDS = [
    (CPU, dict(cores=1, socket='S', power_watts=1), 'cores'),
    (CPU, dict(cores=1, socket='S', power_watts=1), 'power_watts'),
    (Storage, dict(capacity_gb=1), 'capacity_gb'),
]


@pytest.mark.parametrize('cls, extra, field', INTEGER_FIELDS)
@pytest.mark.parametrize('value, error', [(True, TypeError), (1.5, TypeError), ('1', TypeError),
                                        (IntChild(1), TypeError), (0, ValueError), (-1, ValueError)])
def test_positive_device_integer_boundaries(cls, extra, field, value, error):
    args = dict(extra)
    args[field] = value
    with pytest.raises(error):
        cls('D', 'A', 1, 0, **args)


def test_minimal_device_integer_success():
    cpu = CPU('C', 'A', 0, 0, 1, 'S', 1)
    assert (cpu.cores, cpu.power_watts) == (1, 1)
    assert Storage('S', 'A', 0, 0, 1).capacity_gb == 1


@pytest.mark.parametrize('value, error', [(None, TypeError), (1, TypeError),
                                        (StrChild('S'), TypeError), ('', ValueError), ('  ', ValueError)])
@pytest.mark.parametrize('kind', ['cpu', 'ssd'])
def test_socket_and_interface_text_policy(kind, value, error):
    with pytest.raises(error):
        if kind == 'cpu':
            CPU('D', 'A', 1, 0, 1, value, 1)
        else:
            SSD('D', 'A', 1, 0, 1, value)


@pytest.mark.parametrize('size', ['2.5"', '3.5"'])
@pytest.mark.parametrize('rpm', [1000, 50000])
def test_hdd_valid_size_and_inclusive_rpm_endpoints(size, rpm):
    disk = HDD('H', 'A', 0, 0, 1, size, rpm)
    assert (disk.size, disk.rpm, disk.capacity_gb) == (size, rpm, 1)


@pytest.mark.parametrize('size, error', [('2.5', ValueError), (' 3.5"', ValueError),
                                       ('4.0"', ValueError), (3.5, TypeError), (StrChild('2.5"'), TypeError)])
def test_hdd_size_policy(size, error):
    with pytest.raises(error):
        HDD('H', 'A', 1, 0, 100, size, 7200)


@pytest.mark.parametrize('rpm, error', [(999, ValueError), (50001, ValueError), (True, TypeError),
                                      (1000.0, TypeError), ('1000', TypeError), (IntChild(1000), TypeError)])
def test_hdd_rpm_policy(rpm, error):
    with pytest.raises(error):
        HDD('H', 'A', 1, 0, 100, '2.5"', rpm)


def test_hdd_initializer_calls_use_one_actual_receiver(monkeypatch):
    seen = []
    resource_init, storage_init, hdd_init = Resource.__init__, Storage.__init__, HDD.__init__

    def watch_resource(self, *args, **kwargs):
        seen.append(('Resource', self))
        resource_init(self, *args, **kwargs)

    def watch_storage(self, *args, **kwargs):
        seen.append(('Storage', self))
        storage_init(self, *args, **kwargs)

    def watch_hdd(self, *args, **kwargs):
        seen.append(('HDD', self))
        hdd_init(self, *args, **kwargs)

    monkeypatch.setattr(Resource, '__init__', watch_resource)
    monkeypatch.setattr(Storage, '__init__', watch_storage)
    monkeypatch.setattr(HDD, '__init__', watch_hdd)
    disk = HDD('H', 'A', 1, 0, 100, '2.5"', 7200)
    assert [label for label, receiver in seen] == ['HDD', 'Storage', 'Resource']
    assert all(receiver is disk for label, receiver in seen)
