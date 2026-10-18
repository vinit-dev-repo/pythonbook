x = "global x"

def outer():
    x = "enclosing x"
    def inner():
        x = "local x"
        print(x)          # reads this function's already-bound local x
    inner()

outer()
print(x)                   # this print is at global scope
