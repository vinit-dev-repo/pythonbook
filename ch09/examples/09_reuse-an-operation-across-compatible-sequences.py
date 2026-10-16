def start_at(sequence, shift):
    if len(sequence) == 0:
        return sequence[:]
    offset = shift % len(sequence)
    return sequence[offset:] + sequence[:offset]

roster = ["west", "east", "north"]
print(start_at(roster, 1))
print(start_at((4, 8, 9), -1))
print(start_at("ABCD", 6))
print(start_at([], 5))
print(roster)
