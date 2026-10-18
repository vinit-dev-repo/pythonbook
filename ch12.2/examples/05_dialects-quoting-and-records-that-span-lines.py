import csv

csv.register_dialect("study_semicolon", delimiter=";", lineterminator="\n")
rows = [
    ["label", "note"],
    ["tea; mint", "first line\nsecond line"],
    ['oat "bar"', "plain"],
]
with open("labels.csv", "w", encoding="utf-8", newline="") as file:
    csv.writer(file, dialect="study_semicolon").writerows(rows)

with open("labels.csv", "r", encoding="utf-8", newline="") as file:
    restored = list(csv.reader(file, dialect="study_semicolon"))

print(restored == rows)
for row in restored:
    print(row)
