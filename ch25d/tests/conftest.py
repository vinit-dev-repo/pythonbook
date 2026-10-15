# tests/conftest.py
import pytest

from app.models.resource import Resource


@pytest.fixture
def values():
    return {"name": " Router ", "manufacturer": " Acme ", "total": 10, "allocated": 3}


@pytest.fixture
def resource(values):
    return Resource(**values)


@pytest.fixture
def bundle(values, resource):
    return values, resource


@pytest.fixture
def claimed_resource(resource):
    resource.claim(2)
    return resource
