def a_function():
    pass

class AClass:
    pass

class CallableThing:
    def __call__(self):
        return "I was called!"

print(callable(a_function))
print(callable(AClass))            # a class itself is callable: calling it makes an instance
print(callable(AClass()))          # a plain instance is NOT callable
print(callable(CallableThing()))   # unless it defines __call__
print(CallableThing()())
