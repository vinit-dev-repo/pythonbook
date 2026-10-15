# exercise_person_boundary.py
import json

from jsonschema import ValidationError

from person_boundary import Person, load_person


def candidate(**changes):
    data = {"__type__": "Person", "name": "Noor", "birthdate": "1999-12-31"}
    data.update(changes)
    return json.dumps(data)


def main():
    current = load_person(candidate())
    original = current
    missing = json.dumps({"__type__": "Person", "name": "Noor"})
    failed = [missing, candidate(admin=True), candidate(birthdate="1999-02-29")]
    for text in failed:
        try:
            current = load_person(text)
        except (ValidationError, ValueError):
            pass
        else:
            raise AssertionError("invalid candidate was accepted")
        assert current is original and current.name == "Noor" and current.birthdate.isoformat() == "1999-12-31"
    current = load_person(candidate(birthdate="2000-02-29"))
    assert current is not original and current.birthdate.isoformat() == "2000-02-29"
    print("failed candidates keep Noor:", True)
    print("valid leap date replaces Noor:", True)


if __name__ == "__main__":
    main()
