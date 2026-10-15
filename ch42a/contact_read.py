# contact_read.py
import shelve

import contact_models


if __name__ == '__main__':
    with shelve.open('contacts', flag='r') as records:
        contact = records['contact:ada']
        print(contact.contact_id, contact.greeting())
