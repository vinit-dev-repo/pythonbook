# test_widget_errors.py
import json
import unittest
from datetime import UTC, datetime, timedelta, timezone

from widget_errors import (WidgetException, Supplier, NotManufactured, ProductionDelayed,
                           ShippingDelayed, Checkout, Inventory, OutOfStock, Pricing,
                           InvalidCoupon, CannotStackCoupon)


FIXED = datetime(2026, 9, 22, 12, 0, tzinfo=UTC)
CASES = [(WidgetException, Exception, 500), (Supplier, WidgetException, 503),
         (NotManufactured, Supplier, 404), (ProductionDelayed, Supplier, 503),
         (ShippingDelayed, Supplier, 503), (Checkout, WidgetException, 400),
         (Inventory, Checkout, 409), (OutOfStock, Inventory, 409),
         (Pricing, Checkout, 400), (InvalidCoupon, Pricing, 400),
         (CannotStackCoupon, Pricing, 409)]


class StringChild(str):
    pass


class EventTests(unittest.TestCase):
    def test_all_classes_defaults_statuses_and_actual_family_catches(self):
        for cls, family, code in CASES:
            with self.subTest(cls=cls.__name__):
                error = cls(clock=lambda: FIXED)
                self.assertEqual(error.args, (cls.internal_default,))
                self.assertEqual(str(error), cls.internal_default)
                self.assertEqual(error.public_message, cls.public_default)
                self.assertEqual(error.status.value, code)
                self.assertTrue(error.status.phrase)
                try:
                    raise error
                except family as caught:
                    self.assertIs(caught, error)

    def test_message_none_empty_custom_and_extra_args_policy(self):
        for cls, _, _ in CASES:
            for message, public in [(None, None), ('', ''), ('internal detail', 'Safe summary')]:
                with self.subTest(cls=cls.__name__, message=message):
                    error = cls(message, 'first detail', 'second detail', public_message=public, clock=lambda: FIXED)
                    internal = cls.internal_default if message is None else message
                    public_value = cls.public_default if public is None else public
                    self.assertEqual(error.args, (internal, 'first detail', 'second detail'))
                    self.assertEqual(str(error), internal)
                    self.assertEqual(error.public_dict()['message'], public_value)
                    self.assertEqual(error.diagnostic()['args'], ('first detail', 'second detail'))
        self.assertEqual(WidgetException(clock=lambda: FIXED).diagnostic()['args'], ())

    def test_invalid_message_and_extra_types_fail_before_clock(self):
        calls = []
        def clock():
            calls.append('clock')
            return FIXED
        for bad in (False, 1, [], StringChild('text')):
            for channel in ('internal', 'public', 'extra'):
                with self.subTest(channel=channel, bad=repr(bad)):
                    with self.assertRaises(TypeError):
                        if channel == 'internal':
                            WidgetException(bad, clock=clock)
                        elif channel == 'public':
                            WidgetException(public_message=bad, clock=clock)
                        else:
                            WidgetException(None, bad, clock=clock)
        self.assertEqual(calls, [])

    def test_clock_once_normalized_and_stable_across_all_views(self):
        calls = []
        local = datetime(2026, 9, 22, 17, 30, tzinfo=timezone(timedelta(hours=5, minutes=30)))
        def clock():
            calls.append('clock')
            return local
        error = OutOfStock(clock=clock)
        self.assertEqual(error.event_time, FIXED)
        self.assertIs(error.event_time.tzinfo, UTC)
        for _ in range(3):
            self.assertEqual(error.public_dict()['timestamp'], FIXED.isoformat())
            self.assertEqual(json.loads(error.to_json()), error.public_dict())
            self.assertEqual(error.diagnostic()['timestamp'], FIXED.isoformat())
        self.assertEqual(calls, ['clock'])
        for name in ('event_time', 'message', 'public_message'):
            with self.assertRaises(AttributeError):
                setattr(error, name, None)
            with self.assertRaises(AttributeError):
                delattr(error, name)

    def test_real_clock_is_aware_utc_within_construction_window(self):
        before = datetime.now(UTC)
        error = WidgetException()
        after = datetime.now(UTC)
        self.assertIs(error.event_time.tzinfo, UTC)
        self.assertLessEqual(before, error.event_time)
        self.assertLessEqual(error.event_time, after)

    def test_public_allowlist_freshness_and_internal_marker_exclusion(self):
        marker = 'SYNTHETIC_PRIVATE_EVENT_17'
        for cls, _, code in CASES:
            for public in (None, 'Please choose another option.', ''):
                with self.subTest(cls=cls.__name__, public=public):
                    error = cls(marker, marker, public_message=public, clock=lambda: FIXED)
                    try:
                        try:
                            raise ValueError(marker)
                        except ValueError as cause:
                            raise error from cause
                    except WidgetException as caught:
                        self.assertIs(caught, error)
                    data = error.public_dict()
                    self.assertEqual(set(data), {'code', 'message', 'timestamp'})
                    self.assertIs(type(data['code']), int)
                    self.assertEqual(data['code'], code)
                    self.assertNotIn(marker, error.to_json())
                    self.assertEqual(json.loads(error.to_json()), data)
                    self.assertIn(marker, error.diagnostic()['message'])
                    self.assertIn(marker, error.diagnostic()['args'])
                    self.assertIn(marker, error.diagnostic()['traceback'])
                    data['message'] = 'changed copy'
                    self.assertNotEqual(error.public_dict()['message'], 'changed copy')

    def test_unraised_raised_chained_state_and_formatter_exhaustion(self):
        error = InvalidCoupon('diagnostic coupon', clock=lambda: FIXED)
        self.assertIsNone(error.__traceback__)
        unraised = ''.join(error.traceback_lines)
        self.assertIn('InvalidCoupon: diagnostic coupon', unraised)
        self.assertNotIn('Traceback (most recent call last)', unraised)
        local_only = 'SYNTHETIC_LOCAL_VALUE_28'
        try:
            try:
                raise ValueError('underlying coupon check')
            except ValueError as cause:
                raise error from cause
        except Pricing as caught:
            self.assertIs(caught, error)
        self.assertIsNotNone(error.__traceback__)
        self.assertIsInstance(error.__cause__, ValueError)
        iterator = error.traceback_lines
        lines = list(iterator)
        self.assertTrue(lines)
        self.assertEqual(list(iterator), [])
        self.assertEqual(list(error.traceback_lines), lines)
        formatted = ''.join(lines)
        self.assertIn('ValueError: underlying coupon check', formatted)
        self.assertIn('InvalidCoupon: diagnostic coupon', formatted)
        self.assertIn('direct cause', formatted)
        self.assertNotIn(local_only, formatted)
        self.assertEqual(error.event_time, FIXED)

    def test_clock_contract_and_clock_exception_propagation(self):
        with self.assertRaises(TypeError):
            WidgetException(clock=None)
        for value in (None, 'now', datetime(2026, 1, 1)):
            with self.assertRaises(TypeError):
                WidgetException(clock=lambda: value)
        fault = RuntimeError('clock failed')
        def broken_clock():
            raise fault
        with self.assertRaises(RuntimeError) as caught:
            WidgetException(clock=broken_clock)
        self.assertIs(caught.exception, fault)


if __name__ == '__main__':
    unittest.main(verbosity=2)
