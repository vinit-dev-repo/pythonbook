from annotationlib import Format, get_annotations

def send(order: Order, when: Timestamp) -> Receipt:
    return "pretend receipt"

print("the def itself worked, even though none of those names exist")
print(get_annotations(send, format=Format.STRING))
