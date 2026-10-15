# forwarding_reuse.py
from attribute_policy import Public
from reading_list import ReadingList
from operator_policy import ALLOWED, CheckedReadingList, DeniedAddReadingList


OPERATION_NAMES = ('__str__', '__add__', '__getitem__', '__call__', '__iter__')


class TargetBridge:
    @property
    def _wrapped(self):
        return object.__getattribute__(self, '_Controlled__target')


class ValidatingOpsMixin:
    def __str__(self):
        return self.__getattr__('__str__')()

    def __add__(self, other):
        return self.__getattr__('__add__')(other)

    def __getitem__(self, index):
        return self.__getattr__('__getitem__')(index)

    def __call__(self, *args, **kwargs):
        return self.__getattr__('__call__')(*args, **kwargs)

    def __iter__(self):
        return self.__getattr__('__iter__')()


class DirectOpsMixin:
    def __str__(self):
        return self._wrapped.__str__()

    def __add__(self, other):
        return self._wrapped.__add__(other)

    def __getitem__(self, index):
        return self._wrapped.__getitem__(index)

    def __call__(self, *args, **kwargs):
        return self._wrapped.__call__(*args, **kwargs)

    def __iter__(self):
        return self._wrapped.__iter__()


class RoutedOpsMixin:
    def _route(self, name, *args, **kwargs):
        return self.__getattr__(name)(*args, **kwargs)

    def __str__(self):
        return self._route('__str__')

    def __add__(self, other):
        return self._route('__add__', other)

    def __getitem__(self, index):
        return self._route('__getitem__', index)

    def __call__(self, *args, **kwargs):
        return self._route('__call__', *args, **kwargs)

    def __iter__(self):
        return self._route('__iter__')


class ForwardOperation:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance._wrapped, self.name)


class ExplicitDescriptorOps:
    __str__ = ForwardOperation('__str__')
    __add__ = ForwardOperation('__add__')
    __getitem__ = ForwardOperation('__getitem__')
    __call__ = ForwardOperation('__call__')
    __iter__ = ForwardOperation('__iter__')


GeneratedDescriptorOps = type(
    'GeneratedDescriptorOps',
    (),
    {name: ForwardOperation(name) for name in OPERATION_NAMES},
)


def make_wrapper(ops, *allowed_names):
    base = Public(*allowed_names)(ReadingList)

    class Wrapper(ops, TargetBridge, base):
        pass

    return Wrapper


NO_ADD = tuple(name for name in ALLOWED if name != '__add__')
NO_ITER = tuple(name for name in ALLOWED if name != '__iter__')

InlineChecked = CheckedReadingList
DeniedInline = DeniedAddReadingList
ValidatingChecked = make_wrapper(ValidatingOpsMixin, *ALLOWED)
ValidatingDenied = make_wrapper(ValidatingOpsMixin, *NO_ADD)
RoutedChecked = make_wrapper(RoutedOpsMixin, *ALLOWED)
RoutedDenied = make_wrapper(RoutedOpsMixin, *NO_ADD)
RoutedIterDenied = make_wrapper(RoutedOpsMixin, *NO_ITER)
DirectDenied = make_wrapper(DirectOpsMixin, *NO_ADD)
ExplicitDenied = make_wrapper(ExplicitDescriptorOps, *NO_ADD)
GeneratedDenied = make_wrapper(GeneratedDescriptorOps, *NO_ADD)


class MissingConventionHost:
    def __init__(self, target):
        self.target = target


class MissingConventionDirect(DirectOpsMixin, MissingConventionHost):
    pass


class RepairedConventionHost(MissingConventionHost):
    @property
    def _wrapped(self):
        return self.target


class RepairedConventionDirect(DirectOpsMixin, RepairedConventionHost):
    pass
