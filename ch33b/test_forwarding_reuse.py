# test_forwarding_reuse.py
import unittest
from types import MethodType

from operator_policy import (
    ALLOWED, CheckedReadingList, DeniedAddReadingList, DeniedIterReadingList,
)
from forwarding_reuse import (
    OPERATION_NAMES, NO_ADD, NO_ITER, InlineChecked, DeniedInline,
    ValidatingOpsMixin, RoutedOpsMixin, DirectOpsMixin,
    ForwardOperation, ExplicitDescriptorOps, GeneratedDescriptorOps,
    MissingConventionDirect, RepairedConventionDirect, make_wrapper,
)
from reading_list import ReadingList


# Labels remain useful even though the dynamically made classes share a name.
VARIANTS = (
    ('inline', None, True),
    ('validating mixin', ValidatingOpsMixin, True),
    ('router', RoutedOpsMixin, True),
    ('direct mixin', DirectOpsMixin, False),
    ('explicit descriptors', ExplicitDescriptorOps, False),
    ('installed descriptors', GeneratedDescriptorOps, False),
)


class ForwardingReuseTests(unittest.TestCase):
    def target_of(self, wrapper):
        return object.__getattribute__(wrapper, '_Controlled__target')

    def build(self, ops, allowed, titles):
        if ops is None:
            # Use the actual imported inline classes, not a rebuilt substitute.
            classes = {
                ALLOWED: CheckedReadingList,
                NO_ADD: DeniedAddReadingList,
                NO_ITER: DeniedIterReadingList,
            }
            wrapper_type = classes[allowed]
        else:
            wrapper_type = make_wrapper(ops, *allowed)
        return wrapper_type(titles)

    def test_baseline_names_refer_to_the_accepted_classes(self):
        self.assertIs(InlineChecked, CheckedReadingList)
        self.assertIs(DeniedInline, DeniedAddReadingList)

    def test_allowed_operations_and_result_error_contract(self):
        for label, ops, _ in VARIANTS:
            with self.subTest(variant=label):
                wrapper = self.build(ops, ALLOWED, ['A', 'B'])
                target = self.target_of(wrapper)
                right = ['C']
                result = wrapper + right
                self.assertEqual(str(wrapper), 'ReadingList: A, B')
                self.assertEqual(wrapper[1], 'B')
                self.assertEqual(wrapper('> '), '> A, B')
                self.assertEqual(wrapper(prefix='> '), '> A, B')
                self.assertEqual(list(wrapper), ['A', 'B'])
                self.assertEqual(result.summary(), 'A, B, C')
                self.assertIs(type(result), ReadingList)
                self.assertIsNot(result, target)
                self.assertIs(type(wrapper[:]), list)
                self.assertIs(type(wrapper(prefix='> ')), str)
                self.assertEqual(wrapper.summary(), 'A, B')
                self.assertEqual(right, ['C'])
                self.assertEqual(target.summary(), 'A, B')
                self.assertIs(wrapper.__add__(1), NotImplemented)
                with self.assertRaises(TypeError):
                    wrapper + 1
                bad = ['C', 2]
                for operation in (lambda: wrapper.__add__(bad), lambda: wrapper + bad):
                    with self.assertRaisesRegex(TypeError, '^titles must be an exact list of strings$'):
                        operation()
                self.assertEqual(bad, ['C', 2])
                with self.assertRaises(IndexError):
                    wrapper[5]
                with self.assertRaises(TypeError):
                    wrapper['bad']
                with self.assertRaises(ValueError):
                    wrapper[::0]
                with self.assertRaises(TypeError):
                    wrapper('too', 'many')
                with self.assertRaises(TypeError):
                    wrapper(unexpected='keyword')
                with self.assertRaises(TypeError):
                    wrapper(prefix=1)
                self.assertEqual(target.summary(), 'A, B')
                right.append('D')
                self.assertEqual(result.summary(), 'A, B, C')

    def test_independent_raw_iterators_for_every_variant(self):
        for label, ops, _ in VARIANTS:
            with self.subTest(variant=label):
                wrapper = self.build(ops, ALLOWED, ['A', 'B'])
                first, second = iter(wrapper), iter(wrapper)
                self.assertIs(type(first), type(iter([])))
                self.assertIsNot(first, second)
                self.assertIs(iter(first), first)
                self.assertEqual((next(first), next(second), next(first)), ('A', 'A', 'B'))
                for _ in range(2):
                    with self.assertRaises(StopIteration):
                        next(first)
                self.assertEqual(list(second), ['B'])
                self.assertEqual(list(wrapper), ['A', 'B'])
                self.assertEqual([(a, b) for a in wrapper for b in wrapper], [
                    ('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B'),
                ])

    def test_same_denied_add_configuration_checks_or_bypasses(self):
        for label, ops, checks_policy in VARIANTS:
            with self.subTest(variant=label):
                wrapper = self.build(ops, NO_ADD, ['A'])
                target = self.target_of(wrapper)
                original = target.__add__
                calls = []
                right = ['B']

                def observe(receiver, other):
                    self.assertIs(receiver, target)
                    calls.append(tuple(other))
                    return original(other)

                target.__add__ = MethodType(observe, target)
                try:
                    saved = wrapper.__add__
                    self.assertEqual(calls, [])
                    expected_receiver = target if ops in (ExplicitDescriptorOps, GeneratedDescriptorOps) else wrapper
                    self.assertIs(saved.__self__, expected_receiver)
                    for operation in (lambda: saved(right), lambda: wrapper + right):
                        if checks_policy:
                            with self.assertRaisesRegex(TypeError, '^access denied: __add__$'):
                                operation()
                        else:
                            self.assertEqual(operation().summary(), 'A, B')
                    self.assertEqual(calls, [] if checks_policy else [('B',), ('B',)])
                finally:
                    del target.__add__
                self.assertEqual(right, ['B'])
                self.assertEqual(target.summary(), 'A')

    def test_iteration_creation_checks_and_returned_iterator_boundary(self):
        for label, ops, checks_policy in VARIANTS:
            with self.subTest(variant=label):
                wrapper = self.build(ops, NO_ITER, ['A', 'B'])
                target = self.target_of(wrapper)
                original = target.__iter__
                calls = []

                def observe(receiver):
                    self.assertIs(receiver, target)
                    calls.append('created')
                    return original()

                target.__iter__ = MethodType(observe, target)
                try:
                    self.assertEqual(wrapper[0], 'A')
                    for operation in (lambda: wrapper.__iter__(), lambda: iter(wrapper)):
                        if checks_policy:
                            with self.assertRaisesRegex(TypeError, '^access denied: __iter__$'):
                                operation()
                        else:
                            iterator = operation()
                            count = len(calls)
                            self.assertEqual(list(iterator), ['A', 'B'])
                            self.assertEqual(len(calls), count)
                    self.assertEqual(calls, [] if checks_policy else ['created', 'created'])
                finally:
                    del target.__iter__

                # An admitted iterator also leaves all wrapper forms behind.
                admitted = self.build(ops, ALLOWED, ['A'])
                admitted_target = self.target_of(admitted)
                iterator = iter(admitted)

                def forbidden_creation():
                    raise AssertionError('an existing iterator must not request another traversal')

                admitted_target.__iter__ = forbidden_creation
                try:
                    self.assertEqual(list(iterator), ['A'])
                finally:
                    del admitted_target.__iter__

    def test_descriptor_retrieval_then_invocation_for_both_installations(self):
        for ops in (ExplicitDescriptorOps, GeneratedDescriptorOps):
            with self.subTest(variant=ops.__name__):
                wrapper = self.build(ops, NO_ADD, ['A'])
                target = self.target_of(wrapper)
                original = target.__add__
                calls = []

                def observe(receiver, other):
                    self.assertIs(receiver, target)
                    calls.append(tuple(other))
                    return original(other)

                target.__add__ = MethodType(observe, target)
                try:
                    saved = wrapper.__add__
                    self.assertEqual(calls, [])
                    self.assertIs(saved.__self__, target)
                    self.assertEqual(saved(['B']).summary(), 'A, B')
                    self.assertEqual(calls, [('B',)])
                finally:
                    del target.__add__

    def test_class_access_and_distinct_descriptor_names(self):
        for ops in (ExplicitDescriptorOps, GeneratedDescriptorOps):
            with self.subTest(variant=ops.__name__):
                wrapper_type = make_wrapper(ops, *ALLOWED)
                descriptors = [ops.__dict__[name] for name in OPERATION_NAMES]
                self.assertEqual(len({id(item) for item in descriptors}), len(OPERATION_NAMES))
                for name, item in zip(OPERATION_NAMES, descriptors):
                    self.assertIsInstance(item, ForwardOperation)
                    self.assertEqual(item.name, name)
                    self.assertIs(getattr(ops, name), item)
                    self.assertIs(getattr(wrapper_type, name), item)

    def test_missing_convention_repair_and_wrapper_owned_names(self):
        with self.assertRaises(AttributeError):
            MissingConventionDirect(ReadingList(['A'])) + ['B']
        self.assertEqual((RepairedConventionDirect(ReadingList(['A'])) + ['B']).summary(), 'A, B')
        for label, ops, _ in VARIANTS[1:]:
            with self.subTest(variant=label):
                wrapper = self.build(ops, ALLOWED, ['A'])
                target = self.target_of(wrapper)
                target._wrapped = 'target field'
                self.assertIs(wrapper._wrapped, target)
                self.assertEqual(target._wrapped, 'target field')
                self.assertEqual(wrapper.summary(), 'A')
                with self.assertRaisesRegex(TypeError, '^access denied: secret$'):
                    wrapper.secret
        routed = self.build(RoutedOpsMixin, ALLOWED, ['A'])
        self.target_of(routed)._route = 'target field'
        self.assertIs(routed._route.__self__, routed)
        self.assertEqual(routed[0], 'A')


if __name__ == '__main__':
    unittest.main()
