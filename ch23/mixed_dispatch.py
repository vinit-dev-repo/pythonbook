# mixed_dispatch.py
class FinishStage:
    def run(self):
        print("finish")

class FirstStage(FinishStage):
    def run(self):
        print("first")
        super().run()

class SecondStage(FinishStage):
    def run(self):
        print("second")
        super().run()

class MixedStages(FirstStage, SecondStage):
    def run(self):
        SecondStage.run(self)
        FirstStage.run(self)

MixedStages().run()
