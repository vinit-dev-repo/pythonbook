# contact_create.py
import shelve

from contact_models import Contact


if __name__ == '__main__':
    with shelve.open('contacts', flag='n') as records:
        records['contact:ada'] = Contact('contact:ada', 'Ada')
        print(*sorted(records))
