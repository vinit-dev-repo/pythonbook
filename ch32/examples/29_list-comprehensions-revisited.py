x = "outside"
squares = [x * x for x in range(4)]
print(squares)
print(x)      # still "outside" — the comprehension's x was local to it
