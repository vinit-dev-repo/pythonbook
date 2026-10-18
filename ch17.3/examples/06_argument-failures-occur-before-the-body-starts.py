reservation_calls = []

def reserve(code, copies=1, *, shelf):
    reservation_calls.append(code)
    return code, copies, shelf

invalid_calls = [
    ("missing shelf", ("K7",), {}),
    ("duplicate copies", ("K7", 2), {"copies": 3, "shelf": "north"}),
    ("unknown option", ("K7",), {"shelf": "north", "urgent": True}),
    ("non-string key", ("K7",), {7: "north"}),
]
for label, arguments, options in invalid_calls:
    try:
        reserve(*arguments, **options)
    except TypeError:
        print(label, "rejected")
print("body entries:", reservation_calls)
print(reserve(*["K7"], *(2,), **{"shelf": "north"}))
print("body entries:", reservation_calls)
