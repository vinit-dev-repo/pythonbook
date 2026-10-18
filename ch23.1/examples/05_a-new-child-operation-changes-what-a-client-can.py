class DailyRoutine:
    def run(self):
        return self.study()

class LearnerRoutine(DailyRoutine):
    def study(self):
        return "reading"

print(LearnerRoutine().run())
try:
    print(DailyRoutine().run())
except AttributeError:
    print("AttributeError: base has no study operation")
