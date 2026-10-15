# greetings.py
def hello(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # only runs when this file is executed directly,
    # NOT when another file imports it
    print(hello("World"))
