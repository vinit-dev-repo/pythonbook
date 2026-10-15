# inspect_records.py
from record_models import Manager, Person


class InfoManager(Manager):
    __slots__ = ()
    region = 'north'

    @property
    def label(self):
        return f'{self.name} in {self.region}'


class BriefManager(Manager):
    def gathered_fields(self):
        return (('name', self.name),)


if __name__ == '__main__':
    ada = Person('Ada Lovelace', 'engineer', 50_000)
    mina = Manager('Mina Patel', 100_000)
    print(ada)
    print(mina)
    info = InfoManager('Inez Vega', 90_000)
    print(info)
    print('region' in vars(info), 'label' in vars(info), hasattr(info, '__dict__'))
    brief = BriefManager('Noor Khan', 20_000)
    print(brief)
    brief.gathered_fields = 'shadowed'
    try:
        print(brief)
    except TypeError as error:
        print(type(error).__name__)
    del brief.gathered_fields
    print(brief)
