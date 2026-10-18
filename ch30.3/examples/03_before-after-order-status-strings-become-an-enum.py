def ship_order(status):
    if status == "shpped":   # TYPO -- silently never matches
        print("Sending tracking email...")
    else:
        print("Not shipped yet")

ship_order("shipped")
