class CountdownFrom:
    def __init__(self, start):
        self._start = start

    def __getitem__(self, index):
        value = self._start - index
        if value < 0:
            raise IndexError(index)
        return value

cd = CountdownFrom(3)
for number in cd:
    print(number)

print(2 in cd)
print(10 in cd)
