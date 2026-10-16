class ConfigurableMeta(type):
    def __new__(mcs, name, bases, namespace, track=False, **kwargs):
        cls = super().__new__(mcs, name, bases, namespace, **kwargs)
        cls._tracked = track
        return cls

class Widget(metaclass=ConfigurableMeta, track=True):
    pass

print(Widget._tracked)
