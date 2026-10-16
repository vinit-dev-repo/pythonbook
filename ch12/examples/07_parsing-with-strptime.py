from datetime import datetime

text = "23/08/2026 14:07"
parsed = datetime.strptime(text, "%d/%m/%Y %H:%M")
print(parsed)
print(parsed.year)
