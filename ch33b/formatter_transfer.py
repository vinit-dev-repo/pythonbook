# formatter_transfer.py
from types import MethodType

from attribute_policy import Public
from forwarding_reuse import ForwardOperation, TargetBridge


class Formatter:
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, message):
        return f'{self.prefix}: {message}'

    def __str__(self):
        return f'Formatter({self.prefix})'


# Both forms use this same policy, which does not admit __call__.
FormatterBase = Public('__str__')(Formatter)


class CheckedFormatter(TargetBridge, FormatterBase):
    def __call__(self, message):
        return self.__getattr__('__call__')(message)

    def __str__(self):
        return self.__getattr__('__str__')()


class DirectFormatter(TargetBridge, FormatterBase):
    __call__ = ForwardOperation('__call__')
    __str__ = ForwardOperation('__str__')


if __name__ == '__main__':
    checked = CheckedFormatter('east')
    checked_target = checked._wrapped
    saved_checked = checked.__call__
    assert saved_checked.__self__ is checked
    calls = []

    def guard(receiver, message):
        calls.append(message)
        raise AssertionError('checked target should not be invoked')

    checked_target.__call__ = MethodType(guard, checked_target)
    try:
        for operation in (lambda: saved_checked('ready'), lambda: checked('ready')):
            try:
                operation()
            except TypeError as error:
                assert str(error) == 'access denied: __call__'
            else:
                raise AssertionError('checked call should be refused')
    finally:
        del checked_target.__call__
    assert calls == []
    print('checked saved receiver:', saved_checked.__self__ is checked)
    print('checked calls: explicit and implicit denied')

    left = DirectFormatter('east')
    right = DirectFormatter('west')
    assert type(left) is type(right)
    assert left._wrapped is not right._wrapped
    saved_left = left.__call__
    saved_right = right.__call__
    assert saved_left.__self__ is left._wrapped
    assert saved_right.__self__ is right._wrapped
    assert saved_left('ready') == 'east: ready'
    assert saved_right('ready') == 'west: ready'
    print('direct calls:', saved_left('ready'), saved_right('ready'))
    assert saved_left('again') == 'east: again'
    assert left(message='now') == 'east: now'
    print('first saved again:', saved_left('again'))
    assert str(checked) == str(left) == 'Formatter(east)'
    assert str(right) == 'Formatter(west)'
    print('prefix displays:', str(left), str(right))
