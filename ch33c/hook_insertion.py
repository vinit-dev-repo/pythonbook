# hook_insertion.py
def insert_private(*names):
    private_names = frozenset(names)

    def decorate(record_class):
        def private_getattribute(self, name):
            if name in private_names:
                raise TypeError(f'private read: {name}')
            return object.__getattribute__(self, name)

        def private_setattr(self, name, value):
            if name in private_names:
                raise TypeError(f'private write: {name}')
            object.__setattr__(self, name, value)

        record_class.__getattribute__ = private_getattribute
        record_class.__setattr__ = private_setattr
        return record_class

    return decorate
