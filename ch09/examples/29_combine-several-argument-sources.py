def label_batch(*codes, prefix, separator=" / "):
    return prefix + separator.join(codes)

first_cart = ["A4", "B8"]
second_cart = ("C2",)
settings = {"prefix": "Out: "}
print(label_batch(*first_cart, *second_cart, **settings, separator=" | "))
print(repr(label_batch(**settings)))
