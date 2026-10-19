from typing import Protocol, runtime_checkable


@runtime_checkable
class CallableCharge(Protocol):
    def charge(self, amount: float) -> str: ...


class LabelOnly:
    charge = "not callable"


label = LabelOnly()
print(isinstance(label, CallableCharge))
try:
    label.charge(5)
except TypeError as error:
    print("Failed at call time:", error)
