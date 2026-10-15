# widget_app.py
import logging
from contextlib import contextmanager

from flask import Flask, jsonify
from widget_errors import WidgetException


class CaptureHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.records = []

    def emit(self, record):
        self.records.append(record)


@contextmanager
def capture_logs(logger):
    saved = (logger.handlers[:], logger.level, logger.propagate, logger.disabled)
    handler = CaptureHandler()
    logger.handlers = [handler]
    logger.setLevel(logging.ERROR)
    logger.propagate = False
    logger.disabled = False
    try:
        yield handler.records
    finally:
        logger.handlers, level, logger.propagate, logger.disabled = saved
        logger.setLevel(level)
        handler.close()


def create_app(service, *, logger):
    app = Flask(__name__)
    app.config['TESTING'] = True

    @app.get('/checkout')
    def checkout():
        return jsonify({'result': service()})

    @app.errorhandler(WidgetException)
    def handle_widget_error(error):
        logger.error('event=%s type=%s message=%s details=%r',
                     error.event_time.isoformat(), type(error).__name__,
                     error.message, error.args[1:],
                     exc_info=(type(error), error, error.__traceback__))
        return jsonify(error.public_dict()), error.status.value

    return app
