from annotationlib import Format, get_annotations

def handler(item: "Order") -> None:
    ...

print(get_annotations(handler, format=Format.STRING))
