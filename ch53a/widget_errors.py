# widget_errors.py
import json
from datetime import UTC, datetime
from http import HTTPStatus
from traceback import TracebackException


def utc_now():
    return datetime.now(UTC)


class WidgetException(Exception):
    status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_default = "The widget service encountered an unexpected error."
    public_default = "The widget service could not complete the request."

    def __init__(self, message=None, *diagnostic_args, public_message=None, clock=utc_now):
        if message is not None and type(message) is not str:
            raise TypeError("message must be a string or None")
        if public_message is not None and type(public_message) is not str:
            raise TypeError("public_message must be a string or None")
        if any(type(argument) is not str for argument in diagnostic_args):
            raise TypeError("diagnostic arguments must be strings")
        if not callable(clock):
            raise TypeError("clock must be callable")

        resolved_message = self.internal_default if message is None else message
        resolved_public = self.public_default if public_message is None else public_message
        event_time = clock()
        if not isinstance(event_time, datetime) or event_time.tzinfo is None or event_time.utcoffset() is None:
            raise TypeError("clock must return an aware datetime")

        self._event_time = event_time.astimezone(UTC)
        self._message = resolved_message
        self._public_message = resolved_public
        super().__init__(resolved_message, *diagnostic_args)

    @property
    def event_time(self):
        return self._event_time

    @property
    def message(self):
        return self._message

    @property
    def public_message(self):
        return self._public_message

    def __str__(self):
        return self.message

    def public_dict(self):
        return {
            "code": self.status.value,
            "message": self.public_message,
            "timestamp": self.event_time.isoformat(),
        }

    def to_json(self):
        return json.dumps(self.public_dict())

    @property
    def traceback_lines(self):
        return TracebackException.from_exception(self, capture_locals=False).format()

    def diagnostic(self):
        return {
            "type": type(self).__name__,
            "message": self.message,
            "args": self.args[1:],
            "timestamp": self.event_time.isoformat(),
            "traceback": "".join(self.traceback_lines),
        }


class Supplier(WidgetException):
    status = HTTPStatus.SERVICE_UNAVAILABLE
    internal_default = "The supplier could not provide the widget."
    public_default = "The supplier is temporarily unavailable."


class NotManufactured(Supplier):
    status = HTTPStatus.NOT_FOUND
    internal_default = "The requested widget is not manufactured."
    public_default = "The requested widget was not found."


class ProductionDelayed(Supplier):
    status = HTTPStatus.SERVICE_UNAVAILABLE
    internal_default = "Widget production is delayed."
    public_default = "Widget production is delayed."


class ShippingDelayed(Supplier):
    status = HTTPStatus.SERVICE_UNAVAILABLE
    internal_default = "Widget shipping is delayed."
    public_default = "Widget shipping is delayed."


class Checkout(WidgetException):
    status = HTTPStatus.BAD_REQUEST
    internal_default = "The widget checkout request is invalid."
    public_default = "The checkout request could not be completed."


class Inventory(Checkout):
    status = HTTPStatus.CONFLICT
    internal_default = "The requested widget inventory is unavailable."
    public_default = "The requested widget inventory is unavailable."


class OutOfStock(Inventory):
    status = HTTPStatus.CONFLICT
    internal_default = "The requested widget is out of stock."
    public_default = "The requested widget is out of stock."


class Pricing(Checkout):
    status = HTTPStatus.BAD_REQUEST
    internal_default = "The widget pricing request is invalid."
    public_default = "The pricing request could not be completed."


class InvalidCoupon(Pricing):
    status = HTTPStatus.BAD_REQUEST
    internal_default = "The supplied coupon is invalid."
    public_default = "The coupon cannot be applied."


class CannotStackCoupon(Pricing):
    status = HTTPStatus.CONFLICT
    internal_default = "The supplied coupon cannot be stacked."
    public_default = "The coupon cannot be combined with this order."
