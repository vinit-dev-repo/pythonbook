# test_person_boundary.py
import json

import person_boundary
from jsonschema import ValidationError, validate

def text_for(**changes):
    data = {"__type__": "Person", "name": "Amy", "birthdate": "2000-05-01"}
    data.update(changes)
    return json.dumps(data)

def rejects(value, error, loader=person_boundary.load_person):
    try:
        loader(value)
    except error:
        return
    raise AssertionError(f"expected {error.__name__}")

def check_construction_happens_last():
    original = person_boundary.Person
    calls = []

    class ObservedPerson(original):
        def __init__(self, name, birthdate):
            calls.append((name, birthdate))
            super().__init__(name, birthdate)

    person_boundary.Person = ObservedPerson
    try:
        for value, error in ((3, TypeError), ("{", json.JSONDecodeError),
                             (text_for(admin=True), ValidationError),
                             (text_for(birthdate="2001-02-29"), ValueError)):
            rejects(value, error)
            assert calls == []
        accepted = person_boundary.load_person(text_for())
        assert isinstance(accepted, ObservedPerson) and calls == [("Amy", accepted.birthdate)]
    finally:
        person_boundary.Person = original

def check_hook_is_explicit():
    seen = []
    assert json.loads('{"name": "Amy"}') == {"name": "Amy"}
    assert seen == []
    assert json.loads('{"name": "Amy"}', object_hook=lambda data: seen.append(data) or data) == {"name": "Amy"}
    assert seen == [{"name": "Amy"}]

def check_extra_field_boundary():
    extra = text_for(admin=True)
    permissive = dict(person_boundary.PERSON_SCHEMA)
    permissive.pop("additionalProperties")
    def permissive_loader(text):
        # Test-only control: the schema no longer rejects extra fields.
        data = json.loads(text)
        validate(instance=data, schema=permissive)
        birthday = person_boundary.date.fromisoformat(data["birthdate"])
        return person_boundary.Person(data["name"], birthday)

    try:
        rejects(extra, ValidationError, loader=permissive_loader)
    except AssertionError as error:
        assert str(error) == "expected ValidationError"
    else:
        raise AssertionError("the rejection check did not expose the bypass")
    rejects(extra, ValidationError)  # same check, repaired boundary

if __name__ == "__main__":
    accepted = person_boundary.load_person(text_for())
    assert accepted.name == "Amy" and accepted.birthdate.isoformat() == "2000-05-01"
    padded = text_for() + " " * (4096 - len(text_for()))
    assert person_boundary.load_person(padded).name == "Amy"
    rejects(text_for() + " " * (4097 - len(text_for())), ValueError)
    rejects(3, TypeError)
    rejects("{", json.JSONDecodeError)
    rejects("[]", ValidationError)
    rejects(json.dumps({"__type__": "Person", "name": "Amy"}), ValidationError)
    rejects(text_for(__type__="Other"), ValidationError)
    rejects(text_for(name=3), ValidationError)
    rejects(text_for(birthdate=3), ValidationError)
    rejects(text_for(name=""), ValidationError)
    rejects(text_for(name="   "), ValueError)
    rejects(text_for(name="x" * 81), ValidationError)
    rejects(text_for(birthdate="2000-5-1"), ValidationError)
    rejects(text_for(birthdate="2001-02-29"), ValueError)
    rejects(text_for(birthdate="2000-W18-1"), ValueError)
    assert person_boundary.load_person(text_for(name="x" * 80)).name == "x" * 80
    assert person_boundary.load_person(text_for(name=" Amy ")).name == " Amy "
    assert person_boundary.load_person(text_for(birthdate="2000-02-29")).birthdate.day == 29
    check_construction_happens_last()
    check_hook_is_explicit()
    check_extra_field_boundary()
    print("boundary rejects invalid text before Person construction")
