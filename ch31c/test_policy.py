# test_policy.py
import unittest

from attribute_policy import Private, Public
from policy_models import Gauge, Profile


class PolicyTests(unittest.TestCase):
    def check_profile(self, factory, allows_new):
        Wrapped = factory('secret') if factory is Private else factory('label', 'reveal', 'rename', 'missing')
        WrappedProfile = Wrapped(Profile)
        first = WrappedProfile('Ada', 'rose')
        second = WrappedProfile('Mina', 'violet')
        self.assertIs(type(first), type(second))
        target = object.__getattribute__(first, '_Controlled__target')
        self.assertIsNot(target, object.__getattribute__(second, '_Controlled__target'))
        self.assertEqual(first.label, 'Ada')
        first.label = 'Ada Visible'
        self.assertEqual(first.label, 'Ada Visible')
        self.assertEqual(target.label, 'Ada Visible')
        self.assertEqual(second.reveal(), 'Mina:violet')
        with self.assertRaises(TypeError):
            first.secret
        with self.assertRaises(TypeError):
            first.secret = 'changed'
        self.assertEqual(first.reveal(), 'Ada Visible:rose')
        if allows_new:
            first.extra = 'ok'
            self.assertEqual(first.extra, 'ok')
        else:
            with self.assertRaises(TypeError):
                first.extra = 'no'
        saved = first.rename
        self.assertIs(saved.__self__, target)
        self.assertEqual(saved('Ada Prime'), 'Ada Prime')
        with self.assertRaises(ValueError):
            first.rename('')
        self.assertEqual(first.reveal(), 'Ada Prime:rose')
        self.assertEqual(second.reveal(), 'Mina:violet')
        with self.assertRaises(AttributeError):
            first.missing

    def test_private(self):
        self.check_profile(Private, True)

    def test_public(self):
        self.check_profile(Public, False)

    def test_slots_property_and_bypass(self):
        wrapped = Public('level', 'report', 'inherited', 'ghost')(Gauge)(10)
        target = object.__getattribute__(wrapped, '_Controlled__target')
        self.assertFalse(hasattr(target, '__dict__'))
        self.assertNotIn('inherited', vars(Gauge))
        self.assertEqual(wrapped.inherited, 'gauge base attribute')
        for endpoint in (0, 100):
            wrapped.level = endpoint
            self.assertEqual(target._level, endpoint)
            self.assertEqual(wrapped.report(), f'level={endpoint}')

        class IntSubclass(int):
            pass

        failures = ((-1, ValueError), (101, ValueError), (True, TypeError),
                    (1.5, TypeError), (IntSubclass(20), TypeError))
        for value, error in failures:
            with self.subTest(value=repr(value), kind=type(value).__name__):
                with self.assertRaises(error):
                    wrapped.level = value
                self.assertEqual(wrapped.level, 100)
        with self.assertRaises(AttributeError):
            wrapped.ghost
        with self.assertRaises(AttributeError):
            wrapped.ghost = 1
        self.assertEqual(wrapped.level, 100)
        self.assertFalse(hasattr(target, 'ghost'))

        profile = Private('secret')(Profile)('Ada', 'rose')
        self.assertEqual(getattr(profile, '__target'), 'target-owned collision value')
        target = object.__getattribute__(profile, '_Controlled__target')
        self.assertEqual(target.secret, 'rose')
        with self.assertRaises(TypeError):
            setattr(profile, '_Controlled__target', None)
        self.assertIs(object.__getattribute__(profile, '_Controlled__target'), target)
        replacement = Profile('Iris', 'blue')
        object.__setattr__(profile, '_Controlled__target', replacement)
        self.assertEqual(profile.reveal(), 'Iris:blue')
        self.assertEqual(target.reveal(), 'Ada:rose')
        for configure, names in ((Private, ()), (Public, ('',)), (Private, (7,))):
            with self.subTest(names=names):
                with self.assertRaises(TypeError):
                    configure(*names)

    def test_separate_decorations_keep_class_and_settings(self):
        private_secret = Private('secret')(Profile)
        private_label = Private('label')(Profile)
        public_profile = Public('label', 'reveal')(Profile)
        self.assertIsNot(private_secret, private_label)
        self.assertIsNot(private_secret, public_profile)
        self.assertEqual(private_label('Ada', 'rose').secret, 'rose')
        with self.assertRaises(TypeError):
            public_profile('Ada', 'rose').secret
        hide_secret = Private('secret')
        CapturedProfile = hide_secret(Profile)
        CapturedGauge = hide_secret(Gauge)
        record = CapturedProfile('Noor', 'amber')
        gauge = CapturedGauge(30)
        self.assertEqual(record.reveal(), 'Noor:amber')
        self.assertEqual(gauge.report(), 'level=30')
        self.assertIs(type(object.__getattribute__(record, '_Controlled__target')), Profile)
        self.assertIs(type(object.__getattribute__(gauge, '_Controlled__target')), Gauge)


if __name__ == '__main__':
    unittest.main()
