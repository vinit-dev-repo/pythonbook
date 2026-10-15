# test_deck.py
import random
import unittest
from collections.abc import MutableSequence

from cards import Card, spades_high
from frenchdeck import FrenchDeck
from mutable_deck import IncompleteFrenchDeck, MutableFrenchDeck
from shuffle_demo import set_card


class DeckTests(unittest.TestCase):
    def test_standard_construction_and_read_fallbacks(self):
        expected = [Card(rank, suit)
                    for suit in ('spades', 'diamonds', 'clubs', 'hearts')
                    for rank in ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')]
        deck = FrenchDeck()
        self.assertEqual(len(deck), 52)
        self.assertEqual(list(deck), expected)
        self.assertEqual(len(set(deck)), 52)
        self.assertEqual(deck[0], Card('2', 'spades'))
        self.assertEqual(deck[-1], Card('A', 'hearts'))
        self.assertIs(type(deck[0]), Card)
        first_slice, second_slice = deck[:3], deck[:3]
        self.assertIs(type(first_slice), list)
        self.assertEqual(first_slice, expected[:3])
        self.assertIsNot(first_slice, second_slice)
        self.assertIs(first_slice[0], deck[0])
        first_slice.clear()
        self.assertEqual(list(deck), expected)
        self.assertEqual(deck[12::13], [Card('A', suit) for suit in ('spades', 'diamonds', 'clubs', 'hearts')])
        self.assertEqual(list(reversed(deck)), expected[::-1])
        self.assertIn(Card('A', 'spades'), deck)
        self.assertNotIn(Card('7', 'beasts'), deck)
        for name in ('__iter__', '__contains__', '__reversed__'):
            self.assertNotIn(name, FrenchDeck.__dict__)
        for position in (52, -53):
            with self.assertRaises(IndexError):
                deck[position]

    def test_choice_and_rank_keys_leave_original_unchanged(self):
        deck = FrenchDeck()
        before = tuple(deck)
        chosen = random.choice(deck)
        self.assertTrue(any(chosen is card for card in deck))
        ranked = sorted(deck, key=spades_high)
        self.assertIs(type(ranked), list)
        self.assertEqual(ranked[0], Card('2', 'clubs'))
        self.assertEqual(ranked[-1], Card('A', 'spades'))
        self.assertEqual([spades_high(card) for card in ranked], list(range(52)))
        self.assertEqual(tuple(deck), before)

    def test_shuffle_patch_reaches_both_existing_instances_and_restores(self):
        first, second = FrenchDeck(), FrenchDeck()
        first_before, second_before = tuple(first), tuple(second)
        with self.assertRaises(TypeError):
            random.shuffle(first)
        self.assertEqual(tuple(first), first_before)
        try:
            FrenchDeck.__setitem__ = set_card
            first[0], first[1] = first[1], first[0]
            self.assertEqual(tuple(first), (first_before[1], first_before[0]) + first_before[2:])
            self.assertEqual(tuple(second), second_before)
            first_changed = tuple(first)
            second[0], second[2] = second[2], second[0]
            self.assertEqual(tuple(second), (second_before[2], second_before[1], second_before[0]) + second_before[3:])
            self.assertEqual(tuple(first), first_changed)
            second_changed = tuple(second)
            self.assertIsNone(random.shuffle(first))
            self.assertEqual(sorted(first), sorted(first_before))
            self.assertEqual(tuple(second), second_changed)
        finally:
            del FrenchDeck.__setitem__
        for deck in (first, second):
            before = tuple(deck)
            with self.assertRaises(TypeError):
                deck[0] = deck[0]
            self.assertEqual(tuple(deck), before)

    def test_mutable_requires_all_five_primitives(self):
        self.assertEqual(IncompleteFrenchDeck.__abstractmethods__, {'__delitem__', 'insert'})
        with self.assertRaises(TypeError):
            IncompleteFrenchDeck()
        self.assertFalse(MutableFrenchDeck.__abstractmethods__)
        for name in ('__len__', '__getitem__', '__setitem__', '__delitem__', 'insert'):
            self.assertIn(name, MutableFrenchDeck.__dict__)

    def test_mutable_construction_and_copies(self):
        a, b, c = Card('2', 'clubs'), Card('3', 'clubs'), Card('4', 'clubs')
        source = [a, b, a]
        deck = MutableFrenchDeck(source)
        copied = deck[:]
        self.assertIs(type(copied), list)
        self.assertIsNot(copied, source)
        self.assertIs(copied[0], deck[0])
        source.append(c)
        self.assertEqual(list(deck), [a, b, a])
        deck[0] = c
        self.assertEqual(source, [a, b, a, c])
        self.assertEqual(copied, [a, b, a])
        copied.clear()
        self.assertEqual(list(deck), [c, b, a])
        self.assertEqual(list(MutableFrenchDeck((a, b))), [a, b])
        self.assertEqual(list(MutableFrenchDeck(iter([a, a]))), [a, a])
        self.assertEqual(list(MutableFrenchDeck()), list(FrenchDeck()))
        other = MutableFrenchDeck()
        changed = MutableFrenchDeck()
        changed.clear()
        self.assertEqual(list(other), list(FrenchDeck()))
        self.assertEqual(list(changed), [])

    def test_native_item_slice_mutation_and_failure_state(self):
        a, b, c, d = [Card(rank, 'clubs') for rank in ('2', '3', '4', '5')]
        deck = MutableFrenchDeck([a, b, a])
        deck[0], deck[-1] = c, d
        self.assertEqual(list(deck), [c, b, d])
        deck[1:2] = [a, a]
        self.assertEqual(list(deck), [c, a, a, d])
        deck[::2] = [b, b]
        self.assertEqual(list(deck), [b, a, b, d])
        with self.assertRaises(ValueError):
            deck[::2] = [a]
        self.assertEqual(list(deck), [b, a, b, d])
        del deck[1:3]
        self.assertEqual(list(deck), [b, d])
        del deck[-1]
        self.assertEqual(list(deck), [b])
        deck.insert(0, a)
        deck.insert(100, c)
        self.assertEqual(list(deck), [a, b, c])
        del deck[::2]
        self.assertEqual(list(deck), [b])

    def test_mutable_inherited_helpers_and_errors(self):
        a, b, c, d = [Card(rank, 'clubs') for rank in ('2', '3', '4', '5')]
        deck = MutableFrenchDeck([a, b, a])
        for name in ('append', 'extend', 'pop', 'remove', 'reverse', 'index', 'count', '__iter__', '__reversed__'):
            self.assertNotIn(name, MutableFrenchDeck.__dict__)
            self.assertIs(getattr(MutableFrenchDeck, name), getattr(MutableSequence, name))
        self.assertFalse(hasattr(deck, 'sort'))
        deck.append(c)
        deck.extend([d, a])
        self.assertEqual(list(deck), [a, b, a, c, d, a])
        self.assertEqual(deck.count(a), 3)
        self.assertEqual(deck.index(a), 0)
        self.assertEqual(deck.pop(), a)
        self.assertEqual(list(deck), [a, b, a, c, d])
        deck.remove(a)
        self.assertEqual(list(deck), [b, a, c, d])
        deck.reverse()
        self.assertEqual(list(deck), [d, c, a, b])
        self.assertEqual(list(reversed(deck)), [b, a, c, d])
        self.assertEqual(sorted(deck, key=spades_high), [a, b, c, d])
        self.assertEqual(list(deck), [d, c, a, b])
        with self.assertRaises(ValueError):
            deck.remove(Card('A', 'spades'))
        self.assertEqual(list(deck), [d, c, a, b])
        empty = MutableFrenchDeck([])
        with self.assertRaises(IndexError):
            empty.pop()
        with self.assertRaises(ValueError):
            empty.remove(a)
        self.assertEqual(list(empty), [])

    def test_mutable_shuffle_preserves_current_occurrences_without_patch(self):
        self.assertFalse(hasattr(FrenchDeck, '__setitem__'))
        a, b = Card('2', 'clubs'), Card('A', 'spades')
        for deck in (MutableFrenchDeck(), MutableFrenchDeck([a, b, a]), MutableFrenchDeck([])):
            before = sorted(deck)
            self.assertIsNone(random.shuffle(deck))
            self.assertEqual(sorted(deck), before)


if __name__ == '__main__':
    unittest.main()
