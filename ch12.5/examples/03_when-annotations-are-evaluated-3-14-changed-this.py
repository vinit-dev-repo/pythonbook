try:
    send.__annotations__          # this DOES evaluate them
except NameError as error:
    print("asking for the real objects still fails:", error)
