factor = 3

class GlobalScale:
    factor = 10

    def scale(self, value):
        return value * factor

def make_scale(factor):
    class EnclosedScale:
        factor = 10

        def scale(self, value):
            return value * factor
    return EnclosedScale

print(GlobalScale().scale(5))
LocalScale = make_scale(4)
print(LocalScale().scale(5))
