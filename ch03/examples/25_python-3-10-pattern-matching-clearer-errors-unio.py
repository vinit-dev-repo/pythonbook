def describe(day):
    match day:
        case "Sat" | "Sun":
            return "Weekend!"
        case "Mon":
            return "Start of the week"
        case _:
            return "Just another weekday"

print(describe("Sun"))
print(describe("Mon"))
print(describe("Wed"))
