# labels.py
def to_label(name):
    return "item:" + name

def from_label(label):
    return label[5:]
