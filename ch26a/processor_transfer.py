# processor_transfer.py
from processor import END, processor, ListReader


def clean_label(value):
    return value.strip().upper()


class BracketWriter:
    def __init__(self):
        self.text = ''

    def write(self, value):
        if type(value) is not str:
            raise TypeError('value must be a string')
        self.text += '[' + value + ']'


if __name__ == '__main__':
    original = ['  kiwi  ', '', ' pear ']
    reader = ListReader(original)
    writer = BracketWriter()
    assert processor(reader, clean_label, writer) is None
    assert writer.text == '[KIWI][][PEAR]'
    assert original == ['  kiwi  ', '', ' pear ']
    assert reader.read() is END and reader.read() is END
    print('labels:', writer.text)
    print('source unchanged:', original)
    other_reader = ListReader([' plum ', '  '])
    other_writer = BracketWriter()
    assert processor(other_reader, clean_label, other_writer) is None
    assert other_writer.text == '[PLUM][]'
    assert writer.text == '[KIWI][][PEAR]'
    assert other_reader.read() is END
    print('independent labels:', other_writer.text)
    print('first writer retained:', writer.text)
