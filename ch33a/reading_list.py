# reading_list.py
class ReadingList:
    def __init__(self, titles):
        if type(titles) is not list or any(type(title) is not str for title in titles):
            raise TypeError('titles must be an exact list of strings')
        self._titles = list(titles)

    def summary(self):
        return ', '.join(self._titles)

    def __str__(self):
        return f'ReadingList: {self.summary()}'

    def __repr__(self):
        return f'ReadingList({self._titles!r})'

    def __getitem__(self, index):
        return self._titles[index]

    def __call__(self, prefix=''):
        return prefix + self.summary()

    def __add__(self, titles):
        if type(titles) is not list:
            return NotImplemented
        return ReadingList(self._titles + titles)

    def __iter__(self):
        return iter(self._titles)
