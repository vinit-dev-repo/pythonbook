class Dog:
    pass

d = Dog()

print(type(d))      # what made d?  -> the Dog class
print(type(Dog))     # what made Dog? -> type, the metaclass
print(type(type))    # what made type itself?
