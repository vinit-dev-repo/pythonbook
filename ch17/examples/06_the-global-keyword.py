count = 0

def increment():
    global count
    print(count)
    count = count + 1

increment()
increment()
print(count)
