import csv

row = 'Ada,"red, blue",London'
for fields in csv.reader([row]):
    print(fields)
