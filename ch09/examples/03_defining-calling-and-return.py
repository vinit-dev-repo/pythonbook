def check_age(age):
    if age < 0:
        return "invalid age"
    return "valid age"
    print("this line never runs")   # unreachable — return already happened

print(check_age(-5))
print(check_age(20))
