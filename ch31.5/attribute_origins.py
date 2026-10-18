# attribute_origins.py
from inspect import getattr_static

def definition_map(instance, *, include_object=False):
    """List stored definitions, without evaluating their attribute values."""
    layers = []
    try:
        own = vars(instance)
    except TypeError:
        own = {}
    layers.append(("instance", own))
    for index, cls in enumerate(type(instance).__mro__):
        if cls is object and not include_object:
            continue
        layers.append((f"{index}:{cls.__name__}", vars(cls)))
    result = {}
    for owner, namespace in layers:
        for name in namespace:
            result.setdefault(name, []).append(owner)
    return {name: tuple(result[name]) for name in sorted(result)}

def group_by_owner(definitions):
    groups = {}
    for name, owners in sorted(definitions.items()):
        for owner in owners:
            groups.setdefault(owner, []).append(name)
    return groups

class OriginBase:
    __slots__ = ("code",)
    region = "north"

    @property
    def caption(self):
        raise RuntimeError("reading this property runs code")

    def describe(self):
        return "base method"

class OriginCard(OriginBase):
    __slots__ = ("__dict__",)
    __hash__ = None

card = OriginCard()
card.code = "C7"
card.caption_shadow = "ordinary field"
card.__dict__["caption"] = "shadow entry"
card.describe = "instance override"
origins = definition_map(card)
selected = {name: origins[name] for name in ("caption", "code", "describe", "region")}
for name, owners in selected.items():
    print(name, "->", ", ".join(owners))
for owner, names in group_by_owner(selected).items():
    print(owner, "owns", ", ".join(names))
print("static caption:", type(getattr_static(card, "caption")).__name__)
print("static describe:", getattr_static(card, "describe"))
print("static code:", type(getattr_static(card, "code")).__name__)
print("live code:", card.code)
try:
    print(card.caption)
except RuntimeError as error:
    print(type(error).__name__)
print("object included:", "__repr__" in definition_map(card, include_object=True))
