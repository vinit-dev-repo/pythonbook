import sys

entered = []
def reserve(code, count=1, *notes, urgent=False, **details):
    entered.append(code)
    frame = sys._getframe()
    print("bound:", code, count, notes, urgent, details)
    print("same code:", frame.f_code is reserve.__code__)
    del frame

reserve("R7", 2, "aisle", urgent=True, owner="Mina")
before = len(entered)
for arguments, keywords in [((), {}), (("R8",), {"code": "duplicate"})]:
    try:
        reserve(*arguments, **keywords)
    except TypeError:
        print("binding rejected; body entered:", len(entered) != before)
