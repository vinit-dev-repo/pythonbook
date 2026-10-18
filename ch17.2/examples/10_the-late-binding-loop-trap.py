def make_loop_functions():
    functions = []
    for i in range(3):
        functions.append(lambda: i)
    return functions

def make_default_functions():
    functions = []
    for i in range(3):
        functions.append(lambda i=i: i)
    return functions

late_bound = make_loop_functions()
saved_defaults = make_default_functions()
print([f() for f in late_bound])
print([f() for f in saved_defaults])
