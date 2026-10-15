# test_resource_cache.py
import math
import unittest
from itertools import permutations

from fake_transport import FakeResponse, QueueTransport, scripted_counter
from resource_cache import Resource


class FloatChild(float):
    pass


class StrChild(str):
    pass


class BytesChild(bytes):
    pass


class CacheTests(unittest.TestCase):
    def test_one_load_reused_in_every_property_order_and_actual_call_order(self):
        for order in permutations(('body', 'size', 'duration')):
            with self.subTest(order=order):
                events = []
                transport = QueueTransport([FakeResponse(b'abc', events=events)], events=events)
                counter = scripted_counter([10.0, 12.5], events=events)
                resource = Resource(' https://example.test/a ', transport=transport, counter=counter)
                self.assertIsNone(resource.snapshot)
                self.assertEqual((transport.calls, counter.calls), ([], []))
                values = {name: getattr(resource, name) for name in order}
                self.assertEqual(values, dict(body=b'abc', size=3, duration=2.5))
                saved = resource.snapshot
                self.assertEqual(tuple(saved), ('https://example.test/a', b'abc', 3, 2.5))
                self.assertEqual((resource.body, resource.size, resource.duration), (b'abc', 3, 2.5))
                self.assertIs(resource.snapshot, saved)
                self.assertEqual(transport.calls, [('https://example.test/a', (3, 10))])
                self.assertEqual(len(counter.calls), 2)
                self.assertEqual(events, ['counter', 'transport', 'status', 'body', 'counter'])

    def test_empty_bytes_and_zero_duration_are_valid_cached_values(self):
        transport = QueueTransport([FakeResponse(b'')])
        counter = scripted_counter([-2.0, -2.0])
        resource = Resource('empty', transport=transport, counter=counter)
        self.assertEqual((resource.body, resource.size, resource.duration), (b'', 0, 0.0))
        saved = resource.snapshot
        self.assertIsNotNone(saved)
        self.assertEqual(resource.body, b'')
        self.assertIs(resource.snapshot, saved)
        self.assertEqual(len(transport.calls), 1)

    def test_same_url_retains_different_url_invalidates_and_bad_assignment_preserves(self):
        transport = QueueTransport([FakeResponse(b'old'), FakeResponse(b'')])
        counter = scripted_counter([1.0, 2.0, 3.0, 4.0])
        resource = Resource('one', transport=transport, counter=counter)
        self.assertEqual(resource.body, b'old')
        saved = resource.snapshot
        resource.url = '  one '
        self.assertIs(resource.snapshot, saved)
        self.assertEqual(len(transport.calls), 1)
        for bad, error in ((None, TypeError), (3, TypeError), (StrChild('one'), TypeError), ('', ValueError), ('  ', ValueError)):
            with self.subTest(bad=repr(bad)):
                with self.assertRaises(error):
                    resource.url = bad
                self.assertEqual(resource.url, 'one')
                self.assertIs(resource.snapshot, saved)
        resource.url = ' two '
        self.assertEqual(resource.url, 'two')
        self.assertIsNone(resource.snapshot)
        self.assertEqual(len(transport.calls), 1)
        self.assertEqual(resource.body, b'')
        self.assertEqual(tuple(resource.snapshot), ('two', b'', 0, 1.0))
        self.assertEqual(tuple(saved), ('one', b'old', 3, 1.0))

    def test_constructor_url_and_dependency_boundaries(self):
        for bad, error in ((None, TypeError), (1, TypeError), (StrChild('x'), TypeError), ('', ValueError), ('  ', ValueError)):
            with self.assertRaises(error):
                Resource(bad, transport=QueueTransport([]))
        with self.assertRaises(TypeError):
            Resource('x', transport=None)
        with self.assertRaises(TypeError):
            Resource('x', transport=QueueTransport([]), counter=3)

    def test_snapshot_and_derived_properties_are_read_only(self):
        resource = Resource('x', transport=QueueTransport([FakeResponse(b'a')]), counter=scripted_counter([1.0, 2.0]))
        self.assertEqual(resource.body, b'a')
        saved = resource.snapshot
        for name in ('body', 'size', 'duration', 'snapshot'):
            with self.assertRaises(AttributeError):
                setattr(resource, name, None)
            with self.assertRaises(AttributeError):
                delattr(resource, name)
        with self.assertRaises(AttributeError):
            saved.duration = 0
        self.assertIs(resource.snapshot, saved)

    def test_successful_refresh_replaces_the_whole_snapshot_once(self):
        transport = QueueTransport([FakeResponse(b'old'), FakeResponse(b'fresh!')])
        counter = scripted_counter([1.0, 2.5, 4.0, 4.25])
        resource = Resource('x', transport=transport, counter=counter)
        self.assertEqual(resource.body, b'old')
        old = resource.snapshot
        replacement = resource.refresh()
        self.assertIs(replacement, resource.snapshot)
        self.assertIsNot(replacement, old)
        self.assertEqual(tuple(old), ('x', b'old', 3, 1.5))
        self.assertEqual(tuple(replacement), ('x', b'fresh!', 6, 0.25))
        self.assertEqual((resource.body, resource.size, resource.duration), (b'fresh!', 6, 0.25))
        self.assertEqual((len(transport.calls), len(counter.calls)), (2, 4))

    def test_each_dependency_failure_preserves_first_or_existing_state(self):
        for loaded in (False, True):
            for stage in ('start', 'request', 'status', 'body', 'end'):
                with self.subTest(loaded=loaded, stage=stage):
                    fault = RuntimeError(stage + ' failed')
                    response = FakeResponse(b'new', status_error=fault if stage == 'status' else None,
                                            body_error=fault if stage == 'body' else None)
                    responses = ([FakeResponse(b'old')] if loaded else []) + [fault if stage == 'request' else response]
                    samples = ([1.0, 2.5] if loaded else []) + [fault if stage == 'start' else 5.0,
                                                              fault if stage == 'end' else 6.0]
                    transport = QueueTransport(responses)
                    counter = scripted_counter(samples)
                    resource = Resource('x', transport=transport, counter=counter)
                    if loaded:
                        self.assertEqual(resource.body, b'old')
                    old = resource.snapshot
                    with self.assertRaises(RuntimeError) as caught:
                        if loaded:
                            resource.refresh()
                        else:
                            resource.body
                    self.assertIs(caught.exception, fault)
                    self.assertIs(resource.snapshot, old)
                    if loaded:
                        self.assertEqual(tuple(old), ('x', b'old', 3, 1.5))
                        self.assertEqual((resource.body, resource.size, resource.duration), (b'old', 3, 1.5))
                    self.assertEqual(len(transport.calls), int(loaded) + int(stage != 'start'))
                    self.assertEqual(len(counter.calls), 2 * int(loaded) + (2 if stage == 'end' else 1))

    def test_numeric_samples_reject_wrong_types_nonfinite_backwards_and_overflow(self):
        invalid = [(True, TypeError), (1, TypeError), ('1', TypeError), (FloatChild(1), TypeError),
                   (math.nan, ValueError), (math.inf, ValueError), (-math.inf, ValueError)]
        cases = [(bad, 3.0, error, 0, 1) for bad, error in invalid]
        cases += [(1.0, bad, error, 1, 2) for bad, error in invalid]
        cases += [(3.0, 2.0, ValueError, 1, 2), (-1e308, 1e308, ValueError, 1, 2)]
        for start, end, error, requests, samples in cases:
            with self.subTest(start=repr(start), end=repr(end)):
                transport = QueueTransport([FakeResponse(b'ok')])
                counter = scripted_counter([start, end])
                resource = Resource('x', transport=transport, counter=counter)
                with self.assertRaises(error):
                    resource.refresh()
                self.assertIsNone(resource.snapshot)
                self.assertEqual((len(transport.calls), len(counter.calls)), (requests, samples))

    def test_invalid_body_preserves_old_snapshot_and_never_reads_end(self):
        for body in ('text', bytearray(b'abc'), memoryview(b'abc'), BytesChild(b'abc'), None):
            with self.subTest(body=repr(body)):
                transport = QueueTransport([FakeResponse(b'old'), FakeResponse(body)])
                counter = scripted_counter([1.0, 2.5, 5.0])
                resource = Resource('x', transport=transport, counter=counter)
                self.assertEqual(resource.body, b'old')
                saved = resource.snapshot
                with self.assertRaises(TypeError):
                    resource.refresh()
                self.assertIs(resource.snapshot, saved)
                self.assertEqual(tuple(saved), ('x', b'old', 3, 1.5))
                self.assertEqual(len(counter.calls), 3)

    def test_url_change_failure_cannot_publish_old_content_under_new_url_and_retry_works(self):
        transport = QueueTransport([FakeResponse(b'old'), RuntimeError('offline'), FakeResponse(b'')])
        counter = scripted_counter([1.0, 2.0, 3.0, 4.0, 4.5])
        resource = Resource('old', transport=transport, counter=counter)
        self.assertEqual(resource.body, b'old')
        saved = resource.snapshot
        resource.url = 'new'
        with self.assertRaisesRegex(RuntimeError, 'offline'):
            resource.body
        self.assertIsNone(resource.snapshot)
        self.assertEqual(resource.body, b'')
        self.assertEqual(tuple(resource.snapshot), ('new', b'', 0, 0.5))
        self.assertEqual(tuple(saved), ('old', b'old', 3, 1.0))
        self.assertEqual(transport.calls, [('old', (3, 10)), ('new', (3, 10)), ('new', (3, 10))])

    def assert_consistent_failed_refresh(self, resource):
        old = resource.snapshot
        self.assertIsNotNone(old)
        before = tuple(old)
        with self.assertRaisesRegex(RuntimeError, 'offline'):
            resource.refresh()
        self.assertIs(resource.snapshot, old, 'failed refresh replaced published snapshot')
        self.assertEqual(tuple(resource.snapshot), before)

    def test_same_regression_detects_clearing_one_old_metric_before_failure(self):
        class FaultyResource(Resource):
            def refresh(self):
                old = self.snapshot
                if old is not None:
                    self._snapshot = old._replace(duration=0.0)
                return super().refresh()

        def prepared(cls):
            resource = cls('x', transport=QueueTransport([FakeResponse(b'old'), RuntimeError('offline')]),
                           counter=scripted_counter([1.0, 2.5, 3.0]))
            self.assertEqual(resource.body, b'old')
            return resource

        self.assert_consistent_failed_refresh(prepared(Resource))
        faulty = prepared(FaultyResource)
        with self.assertRaisesRegex(AssertionError, 'failed refresh replaced published snapshot'):
            self.assert_consistent_failed_refresh(faulty)
        self.assertEqual(tuple(faulty.snapshot), ('x', b'old', 3, 0.0))


if __name__ == '__main__':
    unittest.main(verbosity=2)
