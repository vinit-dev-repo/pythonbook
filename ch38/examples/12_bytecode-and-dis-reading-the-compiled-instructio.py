import dis

def describe(n):
    if n < 0:
        return "negative"
    return str(n)

dis.dis(describe, show_offsets=True)
