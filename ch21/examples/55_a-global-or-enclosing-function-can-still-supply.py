def make_scale(factor):
    class EnclosedScale:
        def scale(self, value):
            return value * factor
    return EnclosedScale

first_class = make_scale(4)
second_class = make_scale(6)
print(second_class().scale(5))
print(first_class().scale(5))
