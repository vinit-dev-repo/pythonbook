# policy_demo.py
from attribute_policy import Private, Public
from policy_models import Gauge, Profile


if __name__ == '__main__':
    PrivateProfile = Private('secret')(Profile)
    private_one = PrivateProfile('Ada', 'rose')
    private_two = PrivateProfile('Mina', 'violet')
    print(private_one.label, private_one.reveal())
    try:
        print(private_one.secret)
    except TypeError as error:
        print(type(error).__name__)
    try:
        private_one.secret = 'changed'
    except TypeError as error:
        print(type(error).__name__, private_one.reveal())
    private_one.extra = 'allowed new name'
    print(private_one.extra, private_two.label)
    saved = private_one.rename
    print(saved.__self__ is object.__getattribute__(private_one, '_Controlled__target'), saved('Ada Prime'))
    try:
        private_one.rename('')
    except ValueError as error:
        print(type(error).__name__)
    try:
        print(private_one.missing)
    except AttributeError as error:
        print(type(error).__name__)
    print(private_one.__target, object.__getattribute__(private_one, '_Controlled__target').secret)

    PublicProfile = Public('label', 'reveal', 'rename')(Profile)
    public = PublicProfile('Noor', 'amber')
    public.label = 'Noor Prime'
    print(public.label)
    try:
        public.secret = 'changed'
    except TypeError as error:
        print(type(error).__name__, public.reveal())
    try:
        public.extra = 'denied new name'
    except TypeError as error:
        print(type(error).__name__)

    gauge = Public('level', 'report', 'inherited', 'ghost')(Gauge)(10)
    gauge.level = 25
    print(gauge.report(), gauge.inherited)
    try:
        gauge.level = True
    except TypeError as error:
        print(type(error).__name__, gauge.level)
    try:
        gauge.ghost = 1
    except AttributeError as error:
        print(type(error).__name__, gauge.level)
    try:
        print(gauge.ghost)
    except AttributeError as error:
        print(type(error).__name__)
