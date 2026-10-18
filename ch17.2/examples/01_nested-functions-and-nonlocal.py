def make_counter_wrong():
    count = 0
    def increment():
        count = count + 1   # this creates a NEW local "count" inside increment
        return count
    return increment

counter = make_counter_wrong()
print(counter())
print(counter())
