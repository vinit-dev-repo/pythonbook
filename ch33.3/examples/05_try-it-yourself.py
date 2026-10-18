# 1
it = iter([4, 8, 6])
print(max(it))
print(min(it, default="empty"))
numbers = [4, 8, 6]
print(max(numbers), min(numbers))

# 2
class Three:
    def __len__(self):
        return 3

    def __getitem__(self, index):
        if not 0 <= index < 3:
            raise IndexError(index)
        return index * 10

print(list(Three()))
print(20 in Three())
print(list(reversed(Three())))

# 3
letters = iter("hello")
print(sorted(letters))
print(list(letters))
