# frenchdeck.py
from cards import standard_cards


class FrenchDeck:
    def __init__(self):
        self._cards = standard_cards()

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
