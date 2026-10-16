count = 0

def increment():
    print(count)      # you might expect this to print the global count, 0…
    count = count + 1 # …but this line makes "count" LOCAL to the whole function

increment()
