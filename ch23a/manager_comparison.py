# manager_comparison.py
from person import Person, _validate_pay, _validate_rate


class RepeatedCalculationManager(Person):
    def __init__(self, name, pay=0, bonus=0.10):
        self.bonus = _validate_rate(bonus, "bonus")
        super().__init__(name, "manager", pay)

    def giveRaise(self, rate):
        rate = _validate_rate(rate)
        adjusted = rate + self.bonus
        _validate_rate(adjusted, "combined rate")
        candidate = int(self.pay * (1 + adjusted))
        _validate_pay(candidate)
        self.pay = candidate


if __name__ == "__main__":
    manager = RepeatedCalculationManager("Mina Patel", 100_000)
    manager.giveRaise(0.10)
    print(manager.pay)
