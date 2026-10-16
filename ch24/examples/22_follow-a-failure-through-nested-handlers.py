def nested_trial(problem):
    try:
        try:
            raise problem
        except ValueError:
            print("Inner: handled ValueError")
        finally:
            print("Inner: finally")
    except TypeError:
        print("Outer: handled TypeError")
    else:
        print("Outer: else")
    finally:
        print("Outer: finally")
    print("After both statements")

print("ValueError trial")
nested_trial(ValueError("bad value"))
print("TypeError trial")
nested_trial(TypeError("wrong type"))
