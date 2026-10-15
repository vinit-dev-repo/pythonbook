# processor.py
END = object()


def processor(reader, converter, writer):
    while True:
        data = reader.read()
        if data is END:
            return None
        result = converter(data)
        writer.write(result)


class ListReader:
    def __init__(self, records):
        if type(records) not in (list, tuple):
            raise TypeError("records must be a list or tuple")
        for record in records:
            if record is END:
                raise ValueError("records must not contain END")
        self._records = list(records)
        self._index = 0

    def read(self):
        if self._index >= len(self._records):
            return END
        record = self._records[self._index]
        self._index += 1
        return record


class CountdownReader:
    def __init__(self, start):
        if type(start) is not int:
            raise TypeError("start must be an int")
        if start < 0:
            raise ValueError("start must not be negative")
        self._next = start

    def read(self):
        if self._next is None:
            return END
        value = self._next
        if value == 0:
            self._next = None
        else:
            self._next -= 1
        return value


class ListWriter:
    def __init__(self):
        self.items = []

    def write(self, value):
        if type(value) is not str:
            raise TypeError("value must be a string")
        self.items.append(value)
        return None


class TextWriter:
    def __init__(self):
        self.text = ""

    def write(self, value):
        if type(value) is not str:
            raise TypeError("value must be a string")
        self.text += value + "\n"
        return None


def describe(value):
    return f"{type(value).__name__}:{value!r}"
