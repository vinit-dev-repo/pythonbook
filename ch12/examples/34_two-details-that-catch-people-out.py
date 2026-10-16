name = "World"

try:
    print(t"Hello {name}" + "!")
except TypeError as error:
    print("TypeError:", error)
