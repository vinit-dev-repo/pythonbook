def loud(func):
    def wrapper():
        print("About to run the function...")
        func()
        print("...finished running the function.")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = loud(say_hello)   # wrap it by hand
say_hello()
