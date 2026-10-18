class Duck:
    def speak(self):
        return "Quack!"

class Robot:
    def speak(self):
        return "Beep!"

for thing in [SpeakingDog("Rex"), Duck(), Robot()]:
    print(thing.speak())
