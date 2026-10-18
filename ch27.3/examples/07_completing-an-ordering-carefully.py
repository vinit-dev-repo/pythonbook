from functools import total_ordering

@total_ordering
class RankedTask:
    def __init__(self, score):
        self.score = score

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.score == other.score
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self.score < other.score
        return NotImplemented

print(RankedTask(2) <= RankedTask(7))
print(RankedTask(7) > RankedTask(2))
