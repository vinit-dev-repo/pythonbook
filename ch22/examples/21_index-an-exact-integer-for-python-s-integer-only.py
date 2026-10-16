class Position:
    def __init__(self, value):
        self.value = value

    def __index__(self):
        return self.value

position = Position(3)
letters = "ABCDE"

print(bin(position))
print(letters[position])
print(letters[:position])
