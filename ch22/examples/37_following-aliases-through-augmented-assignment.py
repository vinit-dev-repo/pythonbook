class Changing:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, amount):
        self.value += amount
        return self

class Forgetful:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, amount):
        self.value += amount

class Replacing:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, amount):
        return NotImplemented

    def __add__(self, amount):
        return Replacing(self.value + amount)

changing = Changing(2)
old_changing = changing
changing += 3
print(changing is old_changing, old_changing.value)
forgetful = Forgetful(2)
old_forgetful = forgetful
forgetful += 3
print(forgetful is None, old_forgetful.value)
replacing = Replacing(2)
old_replacing = replacing
replacing += 3
print(replacing is old_replacing, replacing.value, old_replacing.value)
