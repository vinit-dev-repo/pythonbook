# hand_transfer.py
from cards import Card, spades_high
from mutable_deck import MutableFrenchDeck


if __name__ == '__main__':
    ace, low = Card('A', 'spades'), Card('2', 'clubs')
    third, fourth = Card('3', 'diamonds'), Card('4', 'hearts')
    supplied = [ace, low, low]
    hand = MutableFrenchDeck(supplied)
    copied_slice = hand[:]
    assert type(copied_slice) is list
    assert copied_slice is not supplied
    assert copied_slice[0] is hand[0]
    hand.append(third)
    hand.extend([fourth])
    popped = hand.pop()
    assert popped == fourth
    hand.remove(low)
    assert list(hand) == [ace, low, third]
    hand.reverse()
    assert list(hand) == [third, low, ace]
    ranked = sorted(hand, key=spades_high)
    assert ranked == [low, third, ace]
    assert list(hand) == [third, low, ace]
    assert supplied == copied_slice == [ace, low, low]
    copied_slice.clear()
    assert supplied == [ace, low, low]
    assert list(hand) == [third, low, ace]
    print('copies independent:', True)
    print('hand ranks:', [card.rank for card in hand])
    print('ranked result:', [card.rank for card in ranked])
    fresh = MutableFrenchDeck()
    assert [card.rank for card in fresh[12::13]] == ['A'] * 4
    fresh[0], fresh[12] = fresh[12], fresh[0]
    assert fresh[0] == ace
    assert fresh[12] == Card('2', 'spades')
    assert [card.rank for card in fresh[12::13]] == ['2', 'A', 'A', 'A']
    print('after swapping 0 and 12:', fresh[0].rank, [card.rank for card in fresh[12::13]])
