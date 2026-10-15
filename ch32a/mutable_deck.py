# mutable_deck.py
import random
from collections.abc import MutableSequence

from cards import Card, standard_cards


class IncompleteFrenchDeck(MutableSequence):
    def __init__(self):
        self._cards = standard_cards()

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        self._cards[position] = value


class MutableFrenchDeck(MutableSequence):
    def __init__(self, cards=None):
        self._cards = standard_cards() if cards is None else list(cards)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        self._cards[position] = value

    def __delitem__(self, position):
        del self._cards[position]

    def insert(self, index, value):
        self._cards.insert(index, value)


if __name__ == '__main__':
    try:
        IncompleteFrenchDeck()
    except TypeError:
        print('missing primitives:', sorted(IncompleteFrenchDeck.__abstractmethods__))
    else:
        raise AssertionError('incomplete class became concrete')
    card = Card('2', 'clubs')
    hand = MutableFrenchDeck([card, card])
    hand.append(Card('3', 'clubs'))
    hand.extend([Card('4', 'clubs')])
    assert hand.pop() == Card('4', 'clubs')
    hand.remove(card)
    hand.reverse()
    assert list(hand) == [Card('3', 'clubs'), card]
    print('inherited helpers:', [value.rank for value in hand], hand.count(card), hand.index(card))
    deck = MutableFrenchDeck()
    before = sorted(deck)
    assert len(deck) == len(set(deck)) == 52
    assert random.shuffle(deck) is None
    assert sorted(deck) == before
    print('mutable shuffle conserved:', len(deck), True)
