class TicketNumber:
    def __init__(self, label: str):
        self.label = label
        self.next_number = 1

    def __call__(self) -> str:
        value = f"{self.label}-{self.next_number}"
        self.next_number += 1
        return value


left = TicketNumber("left")
right = TicketNumber("right")
print(left())
print(left())
print(right())
print(type(left) is TicketNumber)
