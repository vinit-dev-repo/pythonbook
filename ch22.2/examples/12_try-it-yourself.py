from math import gcd

# 1
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __hash__(self):
        divisor = gcd(self.numerator, self.denominator)
        return hash((self.numerator // divisor, self.denominator // divisor))

half = Fraction(1, 2)
same = Fraction(2, 4)
print(half == same)                            # True
print(hash(half) == hash(same))                # True
print(len({half, same}))                       # 1

# 2
class Playlist:
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

playlist = Playlist()
print(bool(playlist))                          # False
playlist.add("Song A")
print(bool(playlist))                          # True

# 3
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

double = Multiplier(2)
print(double(5))                               # 10
print(callable(double))                        # True

# 4
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __format__(self, spec):
        return "$" + format(self.amount, spec)

price = Money(19.5)
print(f"{price:.2f}")                          # $19.50
print(f"{price}")                              # $19.5
