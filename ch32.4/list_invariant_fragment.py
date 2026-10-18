# list_invariant_fragment.py
class ConstructorOnlyUnique(list):
    def __init__(self, values=()):
        super().__init__(UniqueSequence(values))

fragile = ConstructorOnlyUnique([2, 2, 5])
print(fragile)
fragile.append(2)
print(fragile)
