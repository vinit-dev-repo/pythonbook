with open("log.txt", "w", encoding="utf-8") as file:
    file.write("First entry\n")

with open("log.txt", "a", encoding="utf-8") as file:
    file.write("Second entry\n")

with open("log.txt", "r", encoding="utf-8") as file:
    print(file.read())
