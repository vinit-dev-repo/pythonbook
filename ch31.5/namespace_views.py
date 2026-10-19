# namespace_views.py
"""Three inspection policies for trusted demonstration objects."""
from types import FunctionType, MethodType


def short_value(value):
    if type(value) is MethodType:
        return f"<bound {value.__func__.__name__}>"
    if type(value) is FunctionType:
        return f"<function {value.__name__}>"
    if type(value) in (str, int, float, bool, type(None)):
        text = repr(value)
        return text if len(text) <= 60 else text[:57] + "..."
    return f"<{type(value).__name__}>"


def names_in(mapping, include_special=False):
    return [name for name in sorted(mapping)
            if include_special or not (name.startswith("__") and name.endswith("__"))]


def own_rows(obj, include_special=False):
    try:
        fields = vars(obj)
    except TypeError:
        return ["<no instance dictionary>"]
    return [f"{name} = {short_value(fields[name])}"
            for name in names_in(fields, include_special)]


class FieldsView:
    __slots__ = ()

    def __str__(self):
        return "\n".join([f"own {type(self).__name__}", *own_rows(self)])


class InheritedView:
    __slots__ = ()

    def __rows(self):
        rows = []
        for name in names_in(dir(self)):
            try:
                value = getattr(self, name)
            except Exception as error:
                shown = f"<raises {type(error).__name__}>"
            else:
                shown = short_value(value)
            rows.append(f"{name} = {shown}")
        return rows

    def __str__(self):
        return "\n".join([f"visible {type(self).__name__}", *self.__rows()])


class TreeView:
    __slots__ = ()

    def class_report(self, include_special=False):
        lines = [f"instance {type(self).__name__}"]
        lines.extend("  " + row for row in own_rows(self, include_special))
        seen = set()

        def visit(cls, depth):
            prefix = "  " * depth
            identity = id(cls)
            if identity in seen:
                lines.append(prefix + cls.__name__ + " [seen]")
                return
            seen.add(identity)
            lines.append(prefix + cls.__name__)
            namespace = vars(cls)
            for name in names_in(namespace, include_special):
                lines.append(prefix + "  " + name + " = " + short_value(namespace[name]))
            for base in cls.__bases__:
                visit(base, depth + 1)

        visit(type(self), 1)
        return "\n".join(lines)

    def __str__(self):
        return self.class_report()
