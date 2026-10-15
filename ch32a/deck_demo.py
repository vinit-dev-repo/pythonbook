# deck_demo.py
import random

from cards import Card, spades_high
from frenchdeck import FrenchDeck


if __name__ == '__main__':
    deck = FrenchDeck()
    ranked = sorted(deck, key=spades_high)
    chosen = random.choice(deck)
    print('shape:', len(deck), deck[0], deck[-1])
    print('slice:', deck[:3], deck[12::13])
    print('all pairs:', len(set(deck)), tuple(card.rank for card in deck[12::13]))
    print('fallbacks:', len(list(deck)), tuple(reversed(deck))[:2], Card('A', 'spades') in deck, Card('7', 'beasts') not in deck)
    print('choice retained:', chosen in deck, len(deck))
    print('ranked:', ranked[0], ranked[-1], tuple(spades_high(card) for card in ranked) == tuple(range(52)))
    print('original first:', deck[0])
