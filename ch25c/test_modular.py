# test_modular.py
import importlib
import operator
import sys
import unittest

import mod_direct


IMPLEMENTATIONS = (mod_direct,)


class IntSubclass(int):
    pass


class ModularTests(unittest.TestCase):
    def check_value(self, result, cls, value, modulus):
        self.assertIs(type(result), cls)
        self.assertEqual((result.value, result.modulus), (value, modulus))

    def test_construction_normalization_repr_int_and_negation(self):
        for module in IMPLEMENTATIONS:
            M = module.Mod
            with self.subTest(module=module.__name__):
                for number in (-1, 2, 5):
                    value = M(number, 3)
                    self.check_value(value, M, 2, 3)
                    self.assertEqual(repr(value), 'Mod(2, 3)')
                    self.assertEqual(int(value), 2)
                    negative = -value
                    self.check_value(negative, M, 1, 3)
                    self.assertIsNot(negative, value)
                self.check_value(M(10**200 + 1, 10), M, 1, 10)
                self.check_value(M(-(10**200) - 1, 10), M, 9, 10)
                self.check_value(M(-123, 1), M, 0, 1)
                for bad in (True, 1.0, '1', IntSubclass(1)):
                    for args in ((bad, 3), (1, bad)):
                        with self.assertRaises(TypeError):
                            M(*args)
                for modulus in (0, -1):
                    with self.assertRaises(ValueError):
                        M(1, modulus)

    def test_read_only_properties_and_stable_supported_state(self):
        for module in IMPLEMENTATIONS:
            M = module.Mod
            with self.subTest(module=module.__name__):
                value = M(2, 5)
                original_hash = hash(value)
                for name in ('value', 'modulus'):
                    with self.assertRaises(AttributeError):
                        setattr(value, name, 9)
                    with self.assertRaises(AttributeError):
                        delattr(value, name)
                self.check_value(value, M, 2, 5)
                self.assertEqual(hash(value), original_hash)

    def test_equality_congruence_hashes_and_keys(self):
        for module in IMPLEMENTATIONS:
            M = module.Mod
            with self.subTest(module=module.__name__):
                a, b = M(-1, 3), M(5, 3)
                self.assertTrue(a == b and b == a)
                self.assertFalse(a != b)
                self.assertFalse(a == M(2, 4))
                self.assertFalse(M(2, 4) == a)
                self.assertIs(a.__eq__(2), NotImplemented)
                self.assertFalse(a == 2)
                self.assertFalse(2 == a)
                self.assertEqual(hash(a), hash(b))
                self.assertEqual({a: 'value'}[b], 'value')
                self.assertEqual(len({a, b}), 1)
                self.assertNotEqual(hash(2), hash(5))
                for integer in (-1, 2, 5):
                    self.assertTrue(a.is_congruent(integer))
                self.assertFalse(a.is_congruent(1))
                for other in (True, 2.0, '2', IntSubclass(2), b):
                    with self.assertRaises(TypeError):
                        a.is_congruent(other)

    def test_ordering_and_generated_equality_boundaries(self):
        comparisons = (operator.lt, operator.le, operator.gt, operator.ge)
        for module in IMPLEMENTATIONS:
            M = module.Mod
            with self.subTest(module=module.__name__):
                a, b, equal = M(1, 5), M(2, 5), M(6, 5)
                self.assertEqual([op(a, b) for op in comparisons], [True, True, False, False])
                self.assertEqual([op(b, a) for op in comparisons], [False, False, True, True])
                self.assertEqual([op(a, equal) for op in comparisons], [False, True, False, True])
                self.assertIs(a.__lt__(1), NotImplemented)
                for op in comparisons:
                    with self.assertRaises(TypeError):
                        op(a, 1)
                    with self.assertRaises(TypeError):
                        op(1, a)
                    with self.assertRaises(ValueError):
                        op(a, M(1, 7))

    def test_forward_and_reflected_arithmetic(self):
        for module in IMPLEMENTATIONS:
            M = module.Mod
            with self.subTest(module=module.__name__):
                a, b = M(2, 5), M(4, 5)
                original = (a.value, a.modulus, b.value, b.modulus, hash(a), hash(b))
                for result, expected in ((a+b, 1), (a-b, 3), (a*b, 3),
                                         (a+9, 1), (a-9, 3), (a*9, 3),
                                         (9+a, 1), (9-a, 2), (9*a, 3),
                                         (a+(-3), 4), ((-3)-a, 0)):
                    self.check_value(result, M, expected, 5)
                    self.assertIsNot(result, a)
                    self.assertIsNot(result, b)
                self.assertEqual((a.value, a.modulus, b.value, b.modulus, hash(a), hash(b)), original)

    def test_refusal_preserves_real_reflected_participation(self):
        class Right:
            def __radd__(self, left):
                return ('accepted', left)
        for module in IMPLEMENTATIONS:
            with self.subTest(module=module.__name__):
                value = module.Mod(2, 5)
                right = Right()
                self.assertIs(value.__add__(right), NotImplemented)
                marker, retained = value + right
                self.assertEqual(marker, 'accepted')
                self.assertIs(retained, value)

    def test_unsupported_direct_methods_and_final_expressions(self):
        names = ('__add__', '__sub__', '__mul__', '__radd__', '__rsub__', '__rmul__')
        for module in IMPLEMENTATIONS:
            M = module.Mod
            with self.subTest(module=module.__name__):
                value = M(2, 5)
                for other in (True, 2.0, '2', [], IntSubclass(2)):
                    for name in names:
                        self.assertIs(getattr(value, name)(other), NotImplemented)
                    for operation in (operator.add, operator.sub, operator.mul):
                        with self.assertRaises(TypeError):
                            operation(value, other)
                        with self.assertRaises(TypeError):
                            operation(other, value)

    def test_incompatible_moduli_raise_without_mutating_operands(self):
        for module in IMPLEMENTATIONS:
            M = module.Mod
            with self.subTest(module=module.__name__):
                a, b = M(2, 5), M(2, 7)
                before = (a.value, a.modulus, b.value, b.modulus, hash(a), hash(b))
                for name in ('__add__', '__sub__', '__mul__', '__radd__', '__rsub__', '__rmul__'):
                    with self.assertRaisesRegex(ValueError, 'moduli must match'):
                        getattr(a, name)(b)
                self.assertEqual((a.value, a.modulus, b.value, b.modulus, hash(a), hash(b)), before)

    def test_power_has_integer_exponent_not_residue_semantics(self):
        for module in IMPLEMENTATIONS:
            M = module.Mod
            with self.subTest(module=module.__name__):
                base = M(2, 3)
                self.check_value(base**3, M, 2, 3)
                self.check_value(pow(base, 3), M, 2, 3)
                self.check_value(base**0, M, 1, 3)
                self.check_value(M(2, 1)**0, M, 0, 1)
                self.check_value(base**int(M(3, 3)), M, 1, 3)
                for exponent in (True, 3.0, '3', M(3, 3), IntSubclass(3)):
                    self.assertIs(base.__pow__(exponent), NotImplemented)
                    with self.assertRaises(TypeError):
                        base**exponent
                with self.assertRaises(ValueError):
                    base**(-1)
                self.assertIs(base.__pow__(3, 7), NotImplemented)
                with self.assertRaises(TypeError):
                    pow(base, 3, 7)
                with self.assertRaises(TypeError):
                    2**base
                self.check_value(base, M, 2, 3)

    def test_all_augmented_operations_rebind_and_keep_aliases_and_keys(self):
        for module in IMPLEMENTATIONS:
            M = module.Mod
            with self.subTest(module=module.__name__):
                for name, operand, expected in (('add', 4, 2), ('sub', 4, 1),
                                                 ('mul', 4, 6), ('pow', 3, 6),
                                                 ('add', 7, 5)):
                    value = M(5, 7)
                    alias = value
                    keys = {value: 'retained'}
                    before_hash = hash(value)
                    if name == 'add':
                        value += operand
                    elif name == 'sub':
                        value -= operand
                    elif name == 'mul':
                        value *= operand
                    else:
                        value **= operand
                    self.check_value(value, M, expected, 7)
                    self.assertIsNot(value, alias)
                    self.check_value(alias, M, 5, 7)
                    self.assertEqual(hash(alias), before_hash)
                    self.assertEqual(keys[M(12, 7)], 'retained')
                    self.assertIs(list(keys)[0], alias)
                for name in ('__iadd__', '__isub__', '__imul__', '__ipow__'):
                    self.assertFalse(hasattr(M, name))

    def test_failed_augmented_operations_keep_name_and_key(self):
        for module in IMPLEMENTATIONS:
            M = module.Mod
            with self.subTest(module=module.__name__):
                for name in ('add', 'sub', 'mul', 'pow'):
                    value = M(5, 7)
                    alias = value
                    keys = {value: 'saved'}
                    with self.assertRaises(ValueError):
                        if name == 'add':
                            value += M(1, 3)
                        elif name == 'sub':
                            value -= M(1, 3)
                        elif name == 'mul':
                            value *= M(1, 3)
                        else:
                            value **= -1
                    self.assertIs(value, alias)
                    self.check_value(alias, M, 5, 7)
                    self.assertEqual(keys[M(12, 7)], 'saved')

    def assert_power_answer(self, value):
        self.assertEqual(int(value**3), 2, 'exponent was reduced incorrectly')

    def test_known_answer_catches_faulty_exponent_reduction(self):
        for module in IMPLEMENTATIONS:
            M = module.Mod
            with self.subTest(module=module.__name__):
                class BadPower(M):
                    def __pow__(self, exponent, modulo=None):
                        return M(pow(self.value, exponent % self.modulus, self.modulus), self.modulus)
                self.assert_power_answer(M(2, 3))
                with self.assertRaisesRegex(AssertionError, '1 != 2.*exponent was reduced incorrectly'):
                    self.assert_power_answer(BadPower(2, 3))

    def test_modules_do_not_claim_cross_implementation_compatibility(self):
        for left in IMPLEMENTATIONS:
            for right in IMPLEMENTATIONS:
                if left is right:
                    continue
                with self.subTest(left=left.__name__, right=right.__name__):
                    a, b = left.Mod(2, 3), right.Mod(2, 3)
                    self.assertIs(a.__eq__(b), NotImplemented)
                    self.assertFalse(a == b)
                    self.assertIs(a.__add__(b), NotImplemented)
                    with self.assertRaises(TypeError):
                        a + b


if __name__ == '__main__':
    names = ('mod_direct', 'mod_compatible', 'modular')
    if len(sys.argv) != 2 or sys.argv[1] not in (*names, 'all'):
        raise SystemExit('choose mod_direct, mod_compatible, modular or all')
    selected = names if sys.argv[1] == 'all' else (sys.argv[1],)
    IMPLEMENTATIONS = tuple([importlib.import_module(name) for name in selected])
    print('implementations:', ', '.join(selected))
    unittest.main(argv=[sys.argv[0]], verbosity=2)
