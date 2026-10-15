# fields.py
def _bound(value, label, nonnegative=False):
    if value is None:
        return None
    if type(value) is not int:
        raise TypeError(f'{label} must be a built-in int or None')
    if nonnegative and value < 0:
        raise ValueError(f'{label} must not be negative')
    return value

class BaseValidator:

    def __set_name__(self, owner, name):
        self.owner, self.name, self.storage_name = (owner, name, f'_{name}')

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        if self.storage_name not in instance.__dict__:
            raise AttributeError(self.name)
        return instance.__dict__[self.storage_name]

    def validate(self, value):
        pass

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.storage_name] = value

class IntegerField(BaseValidator):

    def __init__(self, min_value=None, max_value=None):
        self.min_value, self.max_value = (_bound(min_value, 'min_value'), _bound(max_value, 'max_value'))
        if (
            self.min_value is not None
            and self.max_value is not None
            and self.min_value > self.max_value
        ):
            raise ValueError('minimum exceeds maximum')

    def validate(self, value):
        if type(value) is not int:
            raise TypeError(f'{self.name} must be a built-in int')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'{self.name} is below minimum')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'{self.name} is above maximum')

class CharField(BaseValidator):

    def __init__(self, min_length=None, max_length=None):
        self.min_length, self.max_length = (_bound(min_length, 'min_length', True), _bound(max_length, 'max_length', True))
        if (
            self.min_length is not None
            and self.max_length is not None
            and self.min_length > self.max_length
        ):
            raise ValueError('minimum exceeds maximum')

    def validate(self, value):
        if type(value) is not str:
            raise TypeError(f'{self.name} must be a built-in str')
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f'{self.name} is too short')
        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(f'{self.name} is too long')
