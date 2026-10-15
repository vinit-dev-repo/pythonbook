# read_change.py
total = 0
while True:
    try:
        reply = input("change or done: ")
    except EOFError:
        break
    if reply == "done":
        break
    try:
        change = int(reply)
    except ValueError:
        print("Enter a whole number.")
        continue
    total += change
    print("total:", total)
print("closed:", total)
