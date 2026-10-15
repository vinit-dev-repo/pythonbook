# binding_demo.py
from fields import IntegerField


if __name__ == "__main__":
    class Normal:
        count = IntegerField(0, 1)

    print(Normal.count.owner.__name__, Normal.count.name)
    late = IntegerField(0, 1)
    Normal.late = late
    try:
        Normal().late = 1
    except AttributeError as error:
        print(type(error).__name__)
    late.__set_name__(Normal, "late")
    item = Normal()
    item.late = 1
    print(late.owner is Normal, late.name, item.late)

    def make_record():
        return type("Record", (), {"left": IntegerField(), "right": IntegerField()})

    first, second = make_record(), make_record()
    print(first is second, first.left is first.right, first.left is second.left)
    assert first is not second
    assert first.left is not first.right
    assert first.left is not second.left
    assert first.right is not second.right
    for owner in (first, second):
        for name in ("left", "right"):
            field = getattr(owner, name)
            assert field.owner is owner
            assert field.name == name
    a, b = first(), first()
    a.left, b.left = 3, 4
    assert (a.left, b.left) == (3, 4)
    shared = IntegerField()
    Alias = type("Alias", (), {"left": shared, "right": shared})
    sample = Alias()
    sample.left = 1
    sample.right = 2
    print(sample.left, sample.right, shared.name)
    Fixed = type("Fixed", (), {"left": IntegerField(), "right": IntegerField()})
    repaired = Fixed()
    repaired.left = 1
    repaired.right = 2
    print(repaired.left, repaired.right, Fixed.left is Fixed.right)
