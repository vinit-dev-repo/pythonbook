name = "Vinit"
# This line would be a SyntaxError before 3.12:
# print(f"Hello, {name.replace("V", "B")}")

# The old workaround: use a different quote style inside
print(f"Hello, {name.replace('V', 'B')}")
