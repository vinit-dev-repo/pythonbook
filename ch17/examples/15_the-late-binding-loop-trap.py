i = 9
print([f() for f in functions])
print(functions[0].__closure__ is None)
