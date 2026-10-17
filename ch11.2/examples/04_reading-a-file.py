with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("apple\nbanana\ncherry\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print("Line:", line.strip())
