# record_fixture.py
def make_record_class():
    class Record:
        def __init__(self, label, secret):
            self.label = label
            self.secret = secret

        def __getattribute__(self, name):
            value = object.__getattribute__(self, name)
            if name == 'label':
                return value.upper()
            return value

        def __setattr__(self, name, value):
            if name == 'label' and value == '':
                raise ValueError('label must not be empty')
            object.__setattr__(self, name, value)

        def reveal(self):
            return self.secret

        def __str__(self):
            return f'Record({self.label})'

    return Record
