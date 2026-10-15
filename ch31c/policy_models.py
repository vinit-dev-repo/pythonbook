# policy_models.py
class ProfileBase:
    inherited = 'profile base attribute'


class Profile(ProfileBase):

    def __init__(self, label, secret):
        self.label = label
        self.secret = secret
        setattr(self, '__target', 'target-owned collision value')

    def reveal(self):
        return f'{self.label}:{self.secret}'

    def rename(self, label):
        if not label:
            raise ValueError('label is required')
        self.label = label
        return self.label


class GaugeBase:
    __slots__ = ()
    inherited = 'gauge base attribute'


class Gauge(GaugeBase):
    __slots__ = ('_level',)

    def __init__(self, level):
        self.level = level

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if type(value) is not int:
            raise TypeError('level must be an exact int')
        if not 0 <= value <= 100:
            raise ValueError('level must be from 0 through 100')
        self._level = value

    def report(self):
        return f'level={self.level}'
