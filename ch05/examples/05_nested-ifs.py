has_ticket = True
age = 15

if has_ticket:
    if age < 16:
        print("Allowed in with an adult.")
    else:
        print("Allowed in alone.")
else:
    print("No entry without a ticket.")
