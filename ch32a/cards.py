# cards.py
from collections import namedtuple


Card = namedtuple('Card', 'rank suit')
RANKS = [str(number) for number in range(2, 11)] + list('JQKA')
SUITS = ['spades', 'diamonds', 'clubs', 'hearts']
SUIT_VALUES = {'clubs': 0, 'diamonds': 1, 'hearts': 2, 'spades': 3}


def standard_cards():
    return [Card(rank, suit) for suit in SUITS for rank in RANKS]


def spades_high(card):
    return RANKS.index(card.rank) * 4 + SUIT_VALUES[card.suit]
