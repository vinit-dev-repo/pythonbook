def greet(name):
    print(f"Hello, {name}!")

greet = repeat(3)(greet)
#        └──┬──┘
#       returns "decorator" first, THEN decorator(greet) runs
