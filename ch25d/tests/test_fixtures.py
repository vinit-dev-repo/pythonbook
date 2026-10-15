# tests/test_fixtures.py
def test_dependency_graph_reuses_actual_inputs_and_object(values, resource, bundle, claimed_resource):
    shared_values, shared_resource = bundle
    assert shared_values is values
    assert shared_resource is resource is claimed_resource
    assert (resource.total, resource.allocated, resource.available) == (10, 5, 5)
    assert vars(resource) is not values
    values['name'] = 'changed input'
    assert shared_values['name'] == 'changed input'
    assert resource.name == 'Router'


def test_one_fresh_fixture_starts_in_the_declared_state(values, resource):
    assert values == dict(name=' Router ', manufacturer=' Acme ', total=10, allocated=3)
    assert (resource.total, resource.allocated, resource.available) == (10, 3, 7)
    values['name'] = 'first test'
    resource.claim(1)


def test_another_fresh_fixture_starts_in_the_declared_state(values, resource):
    assert values == dict(name=' Router ', manufacturer=' Acme ', total=10, allocated=3)
    assert (resource.total, resource.allocated, resource.available) == (10, 3, 7)
    values['name'] = 'second test'
    resource.purchased(2)
