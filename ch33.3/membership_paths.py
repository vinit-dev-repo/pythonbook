# membership_paths.py
class Indexed:
    values = ("A", "B")

    def __getitem__(self, index):
        print("getitem", index)
        return self.values[index]

class Walking(Indexed):
    def __iter__(self):
        print("iter")
        return iter(self.values)

class Direct(Walking):
    def __contains__(self, item):
        print("contains")
        return item in self.values

for kind in (Indexed, Walking, Direct):
    sample = kind()
    print(kind.__name__)
    print("B in:", "B" in sample)
    print("walk:", list(sample))
