# test_widget_app.py
import json
import logging
import unittest
from datetime import UTC, datetime

from flask import Flask, jsonify
from widget_errors import (WidgetException, Supplier, NotManufactured, ProductionDelayed,
                           ShippingDelayed, Checkout, Inventory, OutOfStock, Pricing,
                           InvalidCoupon, CannotStackCoupon)
from widget_service import run_checkout
from widget_app import capture_logs, create_app


FIXED = datetime(2026, 9, 22, 12, 0, tzinfo=UTC)
LEAVES = [(NotManufactured, 404, 'Supplier'), (ProductionDelayed, 503, 'Supplier'),
          (ShippingDelayed, 503, 'Supplier'), (OutOfStock, 409, 'OutOfStock'),
          (InvalidCoupon, 400, 'Pricing'), (CannotStackCoupon, 409, 'Pricing')]


def fail_with(error):
    def operation():
        raise error
    return operation


class AdapterTests(unittest.TestCase):
    def assert_error_response(self, response, error):
        self.assertEqual(response.status_code, error.status.value, 'transport status mismatch')
        self.assertEqual(response.get_json(), error.public_dict())
        self.assertEqual(response.mimetype, 'application/json')

    def test_every_leaf_real_status_body_single_log_and_reraised_identity(self):
        for cls, code, branch in LEAVES:
            with self.subTest(cls=cls.__name__):
                error = cls('synthetic internal detail', 'detail-1', clock=lambda: FIXED)
                observations = []
                logger = logging.Logger('widget-test')
                with capture_logs(logger) as records:
                    app = create_app(lambda: run_checkout(fail_with(error), observations), logger=logger)
                    response = app.test_client().get('/checkout')
                    self.assert_error_response(response, error)
                    self.assertEqual(response.status_code, code)
                    self.assertEqual(observations, [branch])
                    self.assertEqual(len(records), 1)
                    record = records[0]
                    self.assertIs(record.exc_info[1], error)
                    self.assertIs(record.exc_info[2], error.__traceback__)
                    self.assertEqual(record.exc_info[0], cls)
                    self.assertEqual(record.levelno, logging.ERROR)
                    self.assertEqual(record.name, 'widget-test')
                    self.assertIn(FIXED.isoformat(), record.getMessage())
                    self.assertIn('detail-1', record.getMessage())
                    formatted = logging.Formatter('%(message)s').format(record)
                    self.assertIn(cls.__name__, formatted)
                    self.assertIn('Traceback (most recent call last)', formatted)

    def test_intermediate_family_catches_and_same_exception(self):
        for cls, branch in [(Supplier, 'Supplier'), (Checkout, 'Checkout'),
                            (Inventory, 'Inventory'), (Pricing, 'Pricing')]:
            error = cls(clock=lambda: FIXED)
            observations = []
            with self.assertRaises(cls) as caught:
                run_checkout(fail_with(error), observations)
            self.assertIs(caught.exception, error)
            self.assertEqual(observations, [branch])

    def test_success_has_no_error_record(self):
        logger = logging.Logger('widget-success')
        observations = []
        with capture_logs(logger) as records:
            app = create_app(lambda: run_checkout(lambda: 'accepted', observations), logger=logger)
            response = app.test_client().get('/checkout')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_json(), {'result': 'accepted'})
            self.assertEqual((records, observations), ([], []))

    def test_unexpected_exception_is_not_swallowed_by_widget_handler(self):
        fault = ValueError('unexpected defect')
        logger = logging.Logger('widget-unexpected')
        with capture_logs(logger) as records:
            app = create_app(fail_with(fault), logger=logger)
            with self.assertRaises(ValueError) as caught:
                app.test_client().get('/checkout')
            self.assertIs(caught.exception, fault)
            self.assertEqual(records, [])

    def test_chained_private_marker_stays_out_of_default_and_safe_public_http(self):
        marker = 'SYNTHETIC_PRIVATE_HTTP_41'
        for public in (None, 'Choose one coupon.', ''):
            error = CannotStackCoupon(marker, marker, public_message=public, clock=lambda: FIXED)
            def operation():
                try:
                    raise ValueError(marker)
                except ValueError as cause:
                    raise error from cause
            logger = logging.Logger('widget-private-check')
            with capture_logs(logger) as records:
                response = create_app(operation, logger=logger).test_client().get('/checkout')
                self.assert_error_response(response, error)
                self.assertNotIn(marker, response.get_data(as_text=True))
                self.assertEqual(json.loads(error.to_json()), response.get_json())
                self.assertEqual(len(records), 1)
                self.assertIn(marker, logging.Formatter().format(records[0]))
                self.assertIsInstance(error.__cause__, ValueError)

    def test_same_response_assertion_detects_body_only_status_bug(self):
        error = InvalidCoupon(clock=lambda: FIXED)
        bad = Flask('bad-status-control')
        @bad.get('/checkout')
        def checkout():
            return jsonify(error.public_dict())
        response = bad.test_client().get('/checkout')
        self.assertEqual(response.get_json()['code'], 400)
        self.assertEqual(response.status_code, 200)
        with self.assertRaisesRegex(AssertionError, 'transport status mismatch'):
            self.assert_error_response(response, error)
        logger = logging.Logger('widget-fixed-status')
        with capture_logs(logger) as records:
            fixed = create_app(fail_with(error), logger=logger).test_client().get('/checkout')
            self.assert_error_response(fixed, error)
            self.assertEqual(len(records), 1)

    def test_capture_restores_configuration_on_exception_and_does_not_touch_root(self):
        root = logging.getLogger()
        root_state = (root.handlers[:], root.level, root.propagate, root.disabled)
        logger = logging.Logger('widget-restoration')
        original = logging.NullHandler()
        logger.addHandler(original)
        logger.setLevel(logging.DEBUG)
        logger.propagate = True
        logger.disabled = True
        saved = (logger.handlers[:], logger.level, logger.propagate, logger.disabled)
        with self.assertRaisesRegex(RuntimeError, 'leave capture'):
            with capture_logs(logger) as records:
                logger.error('controlled record')
                self.assertEqual(len(records), 1)
                raise RuntimeError('leave capture')
        self.assertEqual((logger.handlers, logger.level, logger.propagate, logger.disabled), saved)
        self.assertIs(logger.handlers[0], original)
        self.assertEqual((root.handlers, root.level, root.propagate, root.disabled), root_state)
        original.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
