# hook_demo.py
from hook_insertion import insert_private
from record_fixture import make_record_class


def caught(label, operation):
    try:
        operation()
    except (TypeError, ValueError) as error:
        print(f'{label}: {type(error).__name__}: {error}')


if __name__ == '__main__':
    Record = make_record_class()
    existing = Record('Ada', 'rose')
    Original = Record
    original_getattribute = Record.__getattribute__
    original_setattr = Record.__setattr__
    print('before label:', existing.label)
    caught('before empty', lambda: setattr(existing, 'label', ''))

    inserted = insert_private('secret', '__str__')(Record)
    print('same class:', inserted is Original, type(existing) is Original)
    print('hooks changed:', Record.__getattribute__ is not original_getattribute, Record.__setattr__ is not original_setattr)
    print('after label:', existing.label)
    existing.label = ''
    print('after empty accepted:', existing.label == '')
    existing.label = 'Noor'
    print('restored label:', existing.label)
    caught('external read', lambda: existing.secret)
    caught('external write', lambda: setattr(existing, 'secret', 'jade'))
    caught('internal reveal', existing.reveal)
    caught('new construction', lambda: Record('Mina', 'violet'))
    print('raw secret unchanged:', object.__getattribute__(existing, 'secret'))
    caught('explicit str', lambda: existing.__str__())
    print('implicit str:', str(existing))
