for name in ("telnetlib", "cgi", "nntplib", "imghdr"):
    try:
        __import__(name)
        print(f"{name:12s} still importable")
    except ImportError:
        print(f"{name:12s} gone")
