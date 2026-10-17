# 1
with open("shopping.txt", "w", encoding="utf-8") as f:
    f.write("milk\nbread\neggs\n")

with open("shopping.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
# milk
# bread
# eggs

# 2
with open("shopping.txt", "a", encoding="utf-8") as f:
    f.write("jam\n")

with open("shopping.txt", "r", encoding="utf-8") as f:
    print(f.read())      # milk, bread, eggs and jam, one per line

# 3
# "w" truncates existing contents; "a" keeps them and adds to the end.
