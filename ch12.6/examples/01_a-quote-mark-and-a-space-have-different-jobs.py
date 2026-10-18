import csv

exported = '~north|annex~| ready | 7'
record = next(csv.reader([exported], delimiter='|', quotechar='~',
                         skipinitialspace=True))
print(record)
print(type(record[2]).__name__)
without_skip = next(csv.reader([exported], delimiter='|', quotechar='~'))
print(repr(without_skip[1]))
