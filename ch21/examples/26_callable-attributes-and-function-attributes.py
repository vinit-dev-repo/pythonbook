from types import FunctionType, ModuleType
import math

def greeting(name):
    return f"Hello, {name}"

print(isinstance(greeting, FunctionType))
print(isinstance(math, ModuleType))
print(greeting("Asha"))
