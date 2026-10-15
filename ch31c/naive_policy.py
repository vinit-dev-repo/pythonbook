# naive_policy.py
from policy_models import Profile


def Private(*names):
    denied = frozenset(names)

    def decorate(target_class):
        class Naive:
            def __init__(self, *args, **kwargs):
                object.__setattr__(self, '__target', target_class(*args, **kwargs))

            def __getattr__(self, name):
                if name in denied:
                    raise TypeError(f'access denied: {name}')
                return getattr(object.__getattribute__(self, '__target'), name)
        return Naive
    return decorate


if __name__ == '__main__':
    wrapped = Private('secret')(Profile)('Ada', 'rose')
    print(type(wrapped.__target).__name__)
