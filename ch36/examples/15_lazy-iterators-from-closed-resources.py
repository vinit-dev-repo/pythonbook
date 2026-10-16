def read_lines():
    with open("diary.txt") as f:
        lines = f.readlines()      # fully read NOW, while the file is open
    return lines                    # a plain list -- safe to use anywhere

for line in read_lines():
    print(line.strip())
