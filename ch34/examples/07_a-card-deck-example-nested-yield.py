def deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["A", "2", "3", "K"]
    for suit in suits:
        for rank in ranks:
            yield f"{rank} of {suit}"

for card in deck():
    print(card)
