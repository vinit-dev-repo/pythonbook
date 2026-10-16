class Speaker:
    def __init__(self, name):
        self.name = name

class SpeakingDog(Speaker):
    def speak(self):
        return "Woof!"

class SpeakingCat(Speaker):
    def speak(self):
        return "Meow!"

for animal in [SpeakingDog("Rex"), SpeakingCat("Tom")]:
    print(animal.speak())
