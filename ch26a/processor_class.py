# processor_class.py
from processor import processor, ListReader, ListWriter, TextWriter


class Pipeline:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def convert(self, value):
        raise NotImplementedError('a subclass must supply conversion')

    def run(self):
        return processor(self.reader, self.convert, self.writer)


class UppercasePipeline(Pipeline):
    def convert(self, value):
        if type(value) is not str:
            raise TypeError('record must be a built-in string')
        return value.upper()


if __name__ == '__main__':
    reader = ListReader(['map', '', 'route'])
    writer = TextWriter()
    job = UppercasePipeline(reader, writer)
    print('borrowed reader:', job.reader is reader)
    print('bound receiver:', job.convert.__self__ is job)
    print('result:', job.run())
    print('text:', repr(writer.text))
    job.run()
    print('after another run:', repr(writer.text))
    items = ListWriter()
    UppercasePipeline(ListReader(['map', '', 'route']), items).run()
    print('other writer:', items.items)
