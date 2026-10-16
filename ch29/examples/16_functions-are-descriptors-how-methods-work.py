def greet(self):
    return f"Hi, I'm {self.name}"

class Person:
    say_hi = greet

p = Person()
p.name = "Vinit"

manual_bind = greet.__get__(p, Person)   # do it by hand
print(manual_bind())
print(p.say_hi())                         # Python does this for you
