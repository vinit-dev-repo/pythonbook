# tests/test_resource.py
import pytest

from app.models.resource import Resource


class IntChild(int):
    pass


class StrChild(str):
    pass


def state(item):
    return item.total, item.allocated, item.available


def snapshot(item):
    return (item.name, item.manufacturer, item.category, state(item), vars(item).copy())


def test_resource_properties_and_display(resource):
    assert (resource.name, resource.manufacturer, resource.category) == ('Router', 'Acme', 'resource')
    assert state(resource) == (10, 3, 7)
    assert str(resource) == 'Router'
    assert repr(resource) == "Resource(name='Router', category='resource', manufacturer='Acme', total=10, allocated=3)"


@pytest.mark.parametrize("field", ['name', 'manufacturer'])
@pytest.mark.parametrize("value, error", [(None, TypeError), (3, TypeError),
                                        (StrChild('R'), TypeError), ('', ValueError), ('  ', ValueError)])
def test_constructor_text_boundaries(values, field, value, error):
    values[field] = value
    with pytest.raises(error):
        Resource(**values)


@pytest.mark.parametrize("field", ['total', 'allocated'])
@pytest.mark.parametrize("value", [True, 1.5, '1', None, IntChild(1)])
def test_constructor_count_types(values, field, value):
    values[field] = value
    with pytest.raises(TypeError):
        Resource(**values)


@pytest.mark.parametrize("total, allocated", [(-1, 0), (1, -1), (1, 2), (0, 1)])
def test_constructor_count_ranges(total, allocated):
    with pytest.raises(ValueError):
        Resource('R', 'A', total, allocated)


@pytest.mark.parametrize("name", ['name', 'manufacturer', 'total', 'allocated', 'available', 'category'])
def test_public_properties_cannot_be_assigned_or_deleted(resource, name):
    before = snapshot(resource)
    with pytest.raises(AttributeError):
        setattr(resource, name, 9)
    with pytest.raises(AttributeError):
        delattr(resource, name)
    assert snapshot(resource) == before


def test_visible_base_trace_and_none_results(resource):
    for action, amount, expected in [('claim', 2, (10, 5, 5)), ('freeup', 1, (10, 4, 6)),
                                     ('died', 2, (8, 2, 6)), ('purchased', 4, (12, 2, 10))]:
        assert getattr(resource, action)(amount) is None
        assert state(resource) == expected


@pytest.mark.parametrize("action", ['claim', 'freeup', 'died', 'purchased'])
@pytest.mark.parametrize("amount, error", [(True, TypeError), (1.5, TypeError), ('1', TypeError),
                                         (None, TypeError), (IntChild(1), TypeError), (0, ValueError), (-1, ValueError)])
def test_rejected_amounts_preserve_complete_state(resource, action, amount, error):
    before = snapshot(resource)
    with pytest.raises(error):
        getattr(resource, action)(amount)
    assert snapshot(resource) == before


@pytest.mark.parametrize("action, amount", [('claim', 8), ('freeup', 4), ('died', 4)])
def test_excessive_amounts_preserve_complete_state(resource, action, amount):
    before = snapshot(resource)
    with pytest.raises(ValueError):
        getattr(resource, action)(amount)
    assert snapshot(resource) == before


def test_exact_success_boundaries_and_zero_pool():
    item = Resource('empty', 'Acme', 0, 0)
    for action in ('claim', 'freeup', 'died'):
        before = snapshot(item)
        with pytest.raises(ValueError):
            getattr(item, action)(1)
        assert snapshot(item) == before
    assert item.purchased(3) is None
    assert state(item) == (3, 0, 3)
    assert item.claim(3) is None
    assert state(item) == (3, 3, 0)
    assert item.freeup(3) is None
    assert state(item) == (3, 0, 3)
    item.claim(3)
    assert item.died(3) is None
    assert state(item) == (0, 0, 0)


class BadResource(Resource):
    def claim(self, amount):
        self._amount(amount)
        self._allocated += amount


def assert_rejects_overallocation(item):
    before = snapshot(item)
    rejected = False
    try:
        item.claim(2)
    except ValueError:
        rejected = True
    assert rejected, 'claim must reject over-allocation'
    assert snapshot(item) == before


def test_same_public_regression_detects_real_overallocation():
    assert_rejects_overallocation(Resource('test', 'Acme', 1, 0))
    faulty = BadResource('test', 'Acme', 1, 0)
    with pytest.raises(AssertionError, match='claim must reject over-allocation'):
        assert_rejects_overallocation(faulty)
    assert state(faulty) == (1, 2, -1)
