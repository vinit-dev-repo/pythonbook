# processor_class_transfer.py
from processor import ListReader, ListWriter, TextWriter
from processor_class import Pipeline


class PrefixPipeline(Pipeline):
    def __init__(self, reader, writer, prefix):
        if type(prefix) is not str:
            raise TypeError('prefix must be a built-in string')
        super().__init__(reader, writer)
        self.prefix = prefix

    def convert(self, value):
        return self.prefix + str(value)


if __name__ == '__main__':
    first = PrefixPipeline(ListReader([0, '']), TextWriter(), '>')
    second = PrefixPipeline(ListReader([False]), ListWriter(), '?')
    assert PrefixPipeline.run is Pipeline.run
    first.run()
    second.run()
    assert first.reader is not second.reader
    assert first.writer is not second.writer
    assert first.writer.text == '>0\n>\n'
    assert second.writer.items == ['?False']
    first.run()
    assert first.writer.text == '>0\n>\n'
    print(repr(first.writer.text))
    print(second.writer.items)
