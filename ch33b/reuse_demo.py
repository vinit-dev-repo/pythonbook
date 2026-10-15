# reuse_demo.py
from forwarding_reuse import (
    InlineChecked,
    DeniedInline,
    ValidatingDenied,
    DirectDenied,
    ExplicitDenied,
    GeneratedDenied,
    MissingConventionDirect,
    RepairedConventionDirect,
    RoutedDenied,
    RoutedIterDenied,
)
from reading_list import ReadingList


def show(label, operation):
    try:
        print(label + ':', operation())
    except (AttributeError, TypeError) as error:
        print(label + ':', type(error).__name__)


if __name__ == '__main__':
    baseline = InlineChecked(['A', 'B'])
    print('inline admitted:', (baseline + ['C']).summary())
    show('inline denied', lambda: DeniedInline(['A', 'B']) + ['C'])
    print('ordinary summary:', baseline.summary())
    checked = ValidatingDenied(['A', 'B'])
    direct = DirectDenied(['A', 'B'])
    saved_checked = checked.__add__
    saved_direct = direct.__add__
    print('checked saved receiver:', saved_checked.__self__ is checked)
    print('direct saved receiver:', saved_direct.__self__ is direct)
    show('checked denied add', lambda: saved_checked(['C']))
    print('direct denied add:', saved_direct(['C']).summary())

    described = ExplicitDenied(['A', 'B'])
    saved_descriptor = described.__add__
    print('descriptor target receiver:', saved_descriptor.__self__ is described._wrapped)
    print('descriptor add:', saved_descriptor(['C']).summary())
    print('class descriptor:', ExplicitDenied.__add__.name)
    print('generated names:', GeneratedDenied.__add__.name, GeneratedDenied.__iter__.name)

    show('missing convention', lambda: MissingConventionDirect(ReadingList(['A'])) + ['B'])
    print('repaired convention:', (RepairedConventionDirect(ReadingList(['A'])) + ['B']).summary())
    show('routed denied add', lambda: RoutedDenied(['A']).__add__(['B']))
    show('routed denied iter', lambda: iter(RoutedIterDenied(['A'])))
