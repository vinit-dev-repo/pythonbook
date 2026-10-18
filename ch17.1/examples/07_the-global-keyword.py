x = "global"

def before_enclosing_value():
    def read():
        return x
    result = read()
    x = "enclosing"
    return result

try:
    before_enclosing_value()
except NameError:
    print("NameError: enclosing x has no value yet")

def explicit_global_read():
    x = "enclosing"
    def read():
        global x
        return x
    return read()

print(explicit_global_read())
