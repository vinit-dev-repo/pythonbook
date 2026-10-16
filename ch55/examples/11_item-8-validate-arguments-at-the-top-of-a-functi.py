def set_age_bad(age):
    assert age >= 0, "age must not be negative"   # WRONG tool for validating public input
    return age

try:
    print(set_age_bad(-5))
except AssertionError as e:
    print("caught:", e)
