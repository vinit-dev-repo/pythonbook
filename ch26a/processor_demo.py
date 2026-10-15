# processor_demo.py
from processor import END, processor, ListReader, CountdownReader, ListWriter, TextWriter, describe


if __name__ == '__main__':
    events = []
    source = ListReader([0, '', False, None, 'ok'])
    destination = ListWriter()
    class TracedReader:
        def read(self):
            value = source.read()
            events.append(('read', 'END' if value is END else describe(value)))
            return value
    def traced_conversion(value):
        result = describe(value)
        events.append(('convert', result))
        return result
    class TracedWriter:
        def write(self, value):
            events.append(('write', value))
            destination.write(value)
    assert processor(TracedReader(), traced_conversion, TracedWriter()) is None
    for operation, value in events:
        print(operation + ':', value)
    assert destination.items == ['int:0', "str:''", 'bool:False', 'NoneType:None', "str:'ok'"]
    print('list output:', destination.items)
    text = TextWriter()
    processor(ListReader([0, '', False, None, 'ok']), describe, text)
    assert text.text == "int:0\nstr:''\nbool:False\nNoneType:None\nstr:'ok'\n"
    print('text output:', repr(text.text))
    for writer in (ListWriter(), TextWriter()):
        processor(CountdownReader(2), describe, writer)
        if isinstance(writer, ListWriter):
            assert writer.items == ['int:2', 'int:1', 'int:0']
            print('countdown list:', writer.items)
        else:
            assert writer.text == 'int:2\nint:1\nint:0\n'
            print('countdown text:', repr(writer.text))
