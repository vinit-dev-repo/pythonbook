# This class stores no state and has one method
class GreetingMaker:
    def make(self, name):
        return f"Hello, {name}!"

print(GreetingMaker().make("Ana"))

# Pythonic — it's just a function
def make_greeting(name):
    return f"Hello, {name}!"

print(make_greeting("Ana"))
