# display_tools.py
def gathered_fields(instance):
    return tuple(sorted(vars(instance).items()))


def format_fields(fields):
    return ', '.join(f'{name}={value!r}' for name, value in fields)


def captured_display(cls):
    def display(instance):
        return f'[{cls.__name__}: {format_fields(gathered_fields(instance))}]'

    cls.__repr__ = display
    return cls


class AttrDisplay:
    def gathered_fields(self):
        return gathered_fields(self)

    def __repr__(self):
        return f'[{type(self).__name__}: {format_fields(self.gathered_fields())}]'
