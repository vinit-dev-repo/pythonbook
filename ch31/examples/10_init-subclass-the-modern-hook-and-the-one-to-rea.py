class Plugin:
    registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin.registry[cls.__name__] = cls

class CsvExporter(Plugin):
    pass

class JsonExporter(Plugin):
    pass

print(Plugin.registry)
