# account_timezone.py
from datetime import timedelta, timezone


class TimeZone:
    def __init__(self, name, offset_hours=0, offset_minutes=0):
        if type(name) is not str:
            raise TypeError("name must be a string")
        name = name.strip()
        if not name:
            raise ValueError("name must not be blank")
        if type(offset_hours) is not int:
            raise TypeError("offset_hours must be an int")
        if type(offset_minutes) is not int:
            raise TypeError("offset_minutes must be an int")
        if not -59 <= offset_minutes <= 59:
            raise ValueError("offset_minutes must be between -59 and 59")

        total_minutes = offset_hours * 60 + offset_minutes
        if not -720 <= total_minutes <= 840:
            raise ValueError("offset must be between -12:00 and +14:00")

        offset = timedelta(minutes=total_minutes)
        self._name = name
        self._offset = offset
        self._tzinfo = timezone(offset, name)

    @property
    def name(self):
        return self._name

    @property
    def offset(self):
        return self._offset

    @property
    def tzinfo(self):
        return self._tzinfo

    def __eq__(self, other):
        if type(other) is not TimeZone:
            return NotImplemented
        return self.name == other.name and self.offset == other.offset
