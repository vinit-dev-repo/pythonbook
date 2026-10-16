label = "wait / wait / done"
cut = label.find(" / ")
if cut != -1:
    print(label[:cut])
