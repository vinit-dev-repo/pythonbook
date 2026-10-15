# error_transfer.py
import json
import logging
from datetime import UTC, datetime

from widget_errors import CannotStackCoupon
from widget_service import run_checkout
from widget_app import capture_logs, create_app


if __name__ == '__main__':
    fixed = datetime(2026, 10, 5, 8, 15, tzinfo=UTC)
    marker = 'SYNTHETIC_COUPON_DETAIL_73'
    safe = 'Use either SAVE10 or WELCOME, not both.'
    clock_calls = []
    def clock():
        clock_calls.append('clock')
        return fixed
    error = CannotStackCoupon(marker, 'SAVE10 + WELCOME', public_message=safe, clock=clock)
    def operation():
        try:
            raise ValueError(marker)
        except ValueError as cause:
            raise error from cause
    observations = []
    logger = logging.Logger('widget-transfer')
    with capture_logs(logger) as records:
        app = create_app(lambda: run_checkout(operation, observations), logger=logger)
        response = app.test_client().get('/checkout')
        assert observations == ['Pricing']
        assert response.status_code == 409
        assert response.get_json() == {'code': 409, 'message': safe, 'timestamp': fixed.isoformat()}
        assert json.loads(error.to_json()) == response.get_json()
        assert marker not in response.get_data(as_text=True)
        assert len(records) == 1 and records[0].exc_info[1] is error
        assert isinstance(error.__cause__, ValueError)
        assert str(error.__cause__) == marker
        assert marker in logging.Formatter().format(records[0])
        assert error.__traceback__ is not None
        assert error.event_time == fixed and clock_calls == ['clock']
        print('family path:', observations)
        print('transport status:', response.status_code)
        print('public:', error.to_json())
        print('one record and chained cause:', len(records), type(error.__cause__).__name__)
        print('public marker absent:', marker not in response.get_data(as_text=True))
        print('clock calls:', len(clock_calls))
