# shuffle_demo.py
import random

from frenchdeck import FrenchDeck


def set_card(self, position, value):
    self._cards[position] = value


if __name__ == '__main__':
    first, second = FrenchDeck(), FrenchDeck()
    first_before, second_before = tuple(first), tuple(second)
    try:
        random.shuffle(first)
    except TypeError as error:
        assert tuple(first) == first_before
        print('before patch:', type(error).__name__, True)
    else:
        raise AssertionError('read-only shuffle unexpectedly succeeded')
    try:
        FrenchDeck.__setitem__ = set_card
        first[0], first[1] = first[1], first[0]
        assert tuple(second) == second_before
        first_changed = tuple(first)
        second[0], second[2] = second[2], second[0]
        assert tuple(first) == first_changed
        assert first[0] == first_before[1]
        assert second[0] == second_before[2]
        print('both existing decks:', first[0].rank, second[0].rank)
        second_changed = tuple(second)
        assert random.shuffle(first) is None
        assert sorted(first) == sorted(first_before)
        assert tuple(second) == second_changed
        print('shuffle conserved:', len(first), True)
        print('independent changes:', True)
    finally:
        del FrenchDeck.__setitem__
    for deck in (first, second):
        try:
            deck[0] = deck[0]
        except TypeError:
            pass
        else:
            raise AssertionError('item assignment was not restored')
    print('restored assignment refusal:', True)
