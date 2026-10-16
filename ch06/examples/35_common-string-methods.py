text = "  Hello, World!  "
print(text.strip())
print(text.strip().upper())
print(text.strip().lower())

csv_line = "apple,bread,milk"
items = csv_line.split(",")
print(items)
print("-".join(items))

print("cat".replace("c", "b"))
print("banana".find("n"))
print("banana".startswith("ban"))
print("banana".count("a"))
