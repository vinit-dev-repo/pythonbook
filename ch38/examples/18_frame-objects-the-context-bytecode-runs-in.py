import sys

def inner():
    frame = sys._getframe()
    print("code name:", frame.f_code.co_name)
    print("inside function body:", frame.f_lineno > frame.f_code.co_firstlineno)
    print("local names:", list(frame.f_locals.keys()))
    print("caller's function name:", frame.f_back.f_code.co_name)

def outer():
    marker = "outer's own local"
    inner()

outer()
