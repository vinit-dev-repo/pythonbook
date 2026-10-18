def cyclic_starts(values):
    items = tuple(values)
    return (items[offset:] + items[:offset]
            for offset in range(len(items)))

schedule = ["east", "north", "west"]
starts = cyclic_starts(iter(schedule))
schedule.append("south")
print(next(starts))
print(list(starts))
print(list(starts))
print(list(cyclic_starts([])))
