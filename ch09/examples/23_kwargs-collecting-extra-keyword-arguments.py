def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

describe_person(name="Amara", age=21, course="Python")
