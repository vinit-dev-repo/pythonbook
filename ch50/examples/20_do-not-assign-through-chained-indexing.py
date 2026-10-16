# risky: two separate [] steps chained together
sales[sales["city"] == "Tokyo"]["units"] = 0   # does not reliably change sales — see below
