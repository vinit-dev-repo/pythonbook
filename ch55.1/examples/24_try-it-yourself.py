# 1
# There is no single right answer here - the aim is the JUDGEMENT, so mark your
# own rewrite against these three questions:
#   * Does the class hold any state between calls? If not, it is a function.
#   * Is it built in one place and called in one place? Then the class is a
#     detour: GreetingMaker().make("Ana") says nothing that
#     make_greeting("Ana") does not say more directly.
#   * Would a reader have to look at two places (__init__ and the method) to
#     understand one action? A function keeps it in one place.
# Keep the class when there IS real state to hold, when several methods share
# it, or when callers swap implementations behind a common interface.

# 2
from dataclasses import dataclass  # @dataclass needs Python 3.7+
from decimal import Decimal

@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: str

m = Money(Decimal("9.99"), "USD")
print(m)
# m.amount = Decimal("1.00")  # raises: cannot assign to field 'amount'
