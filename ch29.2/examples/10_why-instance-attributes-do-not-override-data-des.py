class Greeter:
    def hello(self):
        return "Hello!"

g = Greeter()
print(g.hello())        # calls the method

g.hello = "not a method anymore"
print(g.hello)           # the instance __dict__ wins now
