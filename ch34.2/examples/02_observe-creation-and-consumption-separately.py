def source():
    print("source called")
    return [4, 7]

def transformed(values):
    print("body started")
    for value in values:
        yield value * 2

def double(value):
    print("double", value)
    return value * 2

function_result = transformed(source())
expression_result = (double(value) for value in source())
print("created")
print(next(function_result))
print(next(expression_result))
