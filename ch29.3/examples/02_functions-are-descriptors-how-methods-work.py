def greet(self):
    return f"Hi, I'm {self.name}"

class Person:
    pass

Person.say_hi = greet   # attach the function as a class attribute

p = Person()
p.name = "Vinit"

bound = p.say_hi          # accessing it runs function.__get__ !
print(type(bound))
print(bound())
