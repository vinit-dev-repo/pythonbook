# evolution_models.py
class Badge:
    def __init__(self, name):
        self.name = name
        self.level = 'new'

    def describe(self):
        return f'v2:{self.name}:{getattr(self, "level", "missing")}'
