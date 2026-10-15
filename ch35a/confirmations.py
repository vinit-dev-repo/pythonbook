# confirmations.py
from collections import namedtuple
from datetime import datetime, timezone

from account_timezone import TimeZone


class ConfirmationError(ValueError):
    pass


def validate_account_id(account_id):
    if type(account_id) is not str:
        raise ConfirmationError("account_id must be a string")
    if not account_id:
        raise ConfirmationError("account_id must not be blank")
    if not account_id.isascii() or not account_id.isalnum():
        raise ConfirmationError("account_id must be ASCII alphanumeric")
    return account_id


def format_confirmation(code, account_id, instant, counter):
    if type(code) is not str or code not in {"D", "W", "I", "X"}:
        raise ConfirmationError("unknown confirmation code")
    account_id = validate_account_id(account_id)
    if not isinstance(instant, datetime) or instant.utcoffset() is None:
        raise ConfirmationError("instant must be aware")
    if type(counter) is not int or counter <= 0:
        raise ConfirmationError("counter must be a positive int")
    utc_instant = instant.astimezone(timezone.utc)
    stamp = (
        f"{utc_instant.year:04d}{utc_instant.month:02d}{utc_instant.day:02d}"
        f"{utc_instant.hour:02d}{utc_instant.minute:02d}{utc_instant.second:02d}"
    )
    return f"{code}-{account_id}-{stamp}-{counter}"


Confirmation = namedtuple(
    "Confirmation", "code account_id utc_time local_time counter"
)


def parse_confirmation(text, preferred_timezone=None):
    try:
        if type(text) is not str:
            raise TypeError("confirmation must be a string")
        if preferred_timezone is None:
            preferred_timezone = TimeZone("UTC")
        elif type(preferred_timezone) is not TimeZone:
            raise TypeError("preferred_timezone must be a TimeZone")

        fields = text.split("-")
        if len(fields) != 4:
            raise ValueError("confirmation must have four fields")
        code, account_id, stamp, counter_text = fields
        if type(code) is not str or code not in {"D", "W", "I", "X"}:
            raise ValueError("unknown confirmation code")
        validate_account_id(account_id)
        if len(stamp) != 14 or not stamp.isascii() or not stamp.isdecimal():
            raise ValueError("timestamp must contain 14 ASCII digits")
        if not counter_text or not counter_text.isascii() or not counter_text.isdecimal():
            raise ValueError("counter must be positive decimal digits")

        utc_time = datetime(
            int(stamp[0:4]), int(stamp[4:6]), int(stamp[6:8]),
            int(stamp[8:10]), int(stamp[10:12]), int(stamp[12:14]),
            tzinfo=timezone.utc,
        )
        counter = int(counter_text)
        if counter <= 0:
            raise ValueError("counter must be positive")
        return Confirmation(
            code, account_id, utc_time,
            utc_time.astimezone(preferred_timezone.tzinfo), counter,
        )
    except (ValueError, TypeError, OverflowError) as error:
        raise ConfirmationError("invalid confirmation") from error
