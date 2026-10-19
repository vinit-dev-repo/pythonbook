def read_lines():
    with open("diary.txt") as f:
        lines = f          # NOT read yet -- f is a lazy iterator over lines
    return lines            # the file is closed the moment we leave "with"!

lines = read_lines()
for line in lines:          # crash -- trying to read a closed file
    print(line)
