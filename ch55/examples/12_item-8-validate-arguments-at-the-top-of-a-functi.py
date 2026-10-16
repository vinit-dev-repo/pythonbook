def set_age_good(age):
    if age < 0:
        raise ValueError(f"age must not be negative, got {age!r}")
    return age

try:
    set_age_good(-5)
except ValueError as e:
    print(e)
