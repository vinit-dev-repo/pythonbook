import re

text = "Call me at 555-1234 or 555-5678."
cleaned = re.sub(r"\d{3}-\d{4}", "[phone number removed]", text)
print(cleaned)
