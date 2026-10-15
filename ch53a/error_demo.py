# error_demo.py
import json
import logging
from datetime import UTC, datetime

from widget_errors import OutOfStock
from widget_service import run_checkout
from widget_app import capture_logs, create_app


if __name__ == '__main__':
    fixed = datetime(2026, 9, 22, 12, 0, tzinfo=UTC)
    error = OutOfStock('stock check found zero units', 'sku-demo', clock=lambda: fixed)
    print('args:', error.args)
    print('unraised:', error.__traceback__ is None)
    print('public:', error.to_json())
    iterator = error.traceback_lines
    assert list(iterator)
    print('same iterator exhausted:', list(iterator) == [])
    print('new iterator has text:', bool(list(error.traceback_lines)))
    observations = []
    def operation():
        raise error
    logger = logging.Logger('widget-demo')
    with capture_logs(logger) as records:
        app = create_app(lambda: run_checkout(operation, observations), logger=logger)
        response = app.test_client().get('/checkout')
        assert response.status_code == 409
        assert response.get_json() == json.loads(error.to_json())
        assert len(records) == 1 and records[0].exc_info[1] is error
        print('family path:', observations)
        print('response status and body code:', response.status_code, response.get_json()['code'])
        print('records and raised stack:', len(records), error.__traceback__ is not None)
        print('event unchanged:', error.event_time == fixed)
