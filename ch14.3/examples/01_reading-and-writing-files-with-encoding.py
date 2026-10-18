with open("cafe.txt", "w", encoding="utf-8") as f:
    n = f.write("café")
print(n)

with open("cafe.txt", encoding="utf-8") as f:
    print(f.read())

# Deliberately choose the wrong encoding to make the failure reproducible.
with open("cafe.txt", encoding="cp1252") as f:
    print(f.read())
