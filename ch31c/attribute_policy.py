# attribute_policy.py
def access_control(fail_if):
    def configure(*names):
        if not names or any(type(name) is not str or not name for name in names):
            raise TypeError('configure one or more nonempty string names')
        configured = frozenset(names)

        def decorate(target_class):
            class Controlled:
                def __init__(self, *args, **kwargs):
                    object.__setattr__(self, '_Controlled__target', target_class(*args, **kwargs))

                def __getattr__(self, name):
                    if fail_if(name, configured):
                        raise TypeError(f'access denied: {name}')
                    return getattr(object.__getattribute__(self, '_Controlled__target'), name)

                def __setattr__(self, name, value):
                    if name == '_Controlled__target':
                        raise TypeError('reserved wrapper name')
                    if fail_if(name, configured):
                        raise TypeError(f'access denied: {name}')
                    setattr(object.__getattribute__(self, '_Controlled__target'), name, value)

            return Controlled

        return decorate

    return configure


Private = access_control(lambda name, names: name in names)
Public = access_control(lambda name, names: name not in names)
