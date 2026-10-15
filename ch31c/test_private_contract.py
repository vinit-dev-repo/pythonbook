# test_private_contract.py
import unittest

from attribute_policy import Private
from policy_models import Profile


class PrivateContract(unittest.TestCase):
    def test_private_read_write_and_target_state(self):
        PrivateProfile = Private('secret')(Profile)
        ada = PrivateProfile('Ada', 'rose')
        mina = PrivateProfile('Mina', 'violet')
        self.assertIs(type(ada), type(mina))
        target = object.__getattribute__(ada, '_Controlled__target')
        self.assertIsNot(target, object.__getattribute__(mina, '_Controlled__target'))
        self.assertEqual(ada.label, 'Ada')
        ada.label = 'Ada Prime'
        self.assertEqual(target.label, 'Ada Prime')
        self.assertEqual(mina.reveal(), 'Mina:violet')
        for operation in ('read', 'write'):
            with self.subTest(operation=operation):
                with self.assertRaises(TypeError):
                    if operation == 'read':
                        getattr(ada, 'secret')
                    else:
                        setattr(ada, 'secret', 'changed')
                self.assertEqual(target.secret, 'rose')
        saved = ada.rename
        self.assertIs(saved.__self__, target)
        self.assertEqual(saved('Ada'), 'Ada')
        with self.assertRaises(ValueError):
            saved('')
        self.assertEqual(target.label, 'Ada')
        self.assertEqual(ada.reveal(), 'Ada:rose')
        ada.extra = 'new field'
        self.assertEqual(target.extra, 'new field')
        self.assertEqual(getattr(ada, '__target'), 'target-owned collision value')
        self.assertEqual(ada.inherited, 'profile base attribute')
        with self.assertRaises(AttributeError):
            ada.missing
        with self.assertRaises(TypeError):
            setattr(ada, '_Controlled__target', None)
        self.assertIs(object.__getattribute__(ada, '_Controlled__target'), target)


if __name__ == '__main__':
    unittest.main()
