# contact_models.py
class Contact:
    def __init__(self, contact_id, name):
        self.contact_id = contact_id
        self.name = name

    def greeting(self):
        return f'Hello {self.name}'
