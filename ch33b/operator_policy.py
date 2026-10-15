# operator_policy.py
from attribute_policy import Public
from reading_list import ReadingList


ALLOWED = ('summary', '__str__', '__add__', '__getitem__', '__call__', '__iter__')


def make_reading_policy(*allowed_names):
    base = Public(*allowed_names)(ReadingList)

    class OperationPolicy(base):
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

    return OperationPolicy


CheckedReadingList = make_reading_policy(*ALLOWED)
DeniedAddReadingList = make_reading_policy(
    'summary', '__str__', '__getitem__', '__call__', '__iter__'
)
DeniedIterReadingList = make_reading_policy(
    'summary', '__str__', '__add__', '__getitem__', '__call__'
)


class DirectAdd(DeniedAddReadingList):
    def __add__(self, other):
        target = object.__getattribute__(self, '_Controlled__target')
        return target.__add__(other)
