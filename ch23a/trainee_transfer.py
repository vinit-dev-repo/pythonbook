# trainee_transfer.py
from person import Department, Person, _validate_rate


class Trainee(Person):
    def __init__(self, name, pay=0):
        self.training_bonus = 0.05
        super().__init__(name, "trainee", pay)

    def giveRaise(self, rate):
        rate = _validate_rate(rate)
        if rate > 0.20:
            raise ValueError("trainee rate must be through 0.20")
        adjusted = rate + self.training_bonus
        _validate_rate(adjusted, "combined trainee rate")
        super().giveRaise(adjusted)


if __name__ == "__main__":
    trainee = Trainee("Rae Kim", 1_000)
    colleague = Person("Noah Vale", pay=1_000)
    Department(trainee, colleague).giveRaises(0.20)
    print(trainee.job, trainee.pay)
    print(colleague.pay)
    before = trainee.pay
    try:
        trainee.giveRaise(0.30)
    except ValueError as error:
        print(error)
    print(trainee.pay == before)
