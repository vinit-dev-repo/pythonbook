# inspect_frameworks.py
import inspect
import tkinter
from django.views.generic import ListView, TemplateView
from django.views.generic.base import View


def defining_class(kind, name):
    for base in kind.__mro__:
        if name in vars(base):
            return base
    raise AttributeError(name)


if __name__ == "__main__":
    for kind in (tkinter.Text, ListView):
        print(kind.__name__, "->", " -> ".join(c.__name__ for c in kind.__mro__))
    for name in ("destroy", "pack", "grid", "xview", "yview"):
        print("Text", name, defining_class(tkinter.Text, name).__name__)
    for name in ("get", "dispatch", "get_queryset", "get_context_data", "render_to_response"):
        print("ListView", name, defining_class(ListView, name).__name__)
    print("View is abstract:", inspect.isabstract(View))
    print("TemplateView defines get:", "get" in vars(TemplateView))
    print("ListView defines get:", "get" in vars(ListView))
