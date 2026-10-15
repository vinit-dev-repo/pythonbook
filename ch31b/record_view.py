# record_view.py
class RecordView:
    def __init__(self, target):
        self.target = target

    def __getattr__(self, name):
        return getattr(self.target, name)

    def __repr__(self):
        return f'[RecordView for {self.target!r}]'
