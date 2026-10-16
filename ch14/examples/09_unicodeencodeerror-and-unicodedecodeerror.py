try:
    chr(0xD800).encode("utf-8")
except UnicodeEncodeError:
    print("UnicodeEncodeError")
