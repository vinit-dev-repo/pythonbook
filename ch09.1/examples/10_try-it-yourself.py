# 1
def is_even(n):
    return n % 2 == 0

print(is_even(4))    # True
print(is_even(7))    # False

# 2
def show(text):
    print(text)

result = show("hi")
print(result)        # hi, then None: show prints but returns nothing

# 3
def shout(text):
    return text.upper() + "!"

def whisper(text):
    return text.lower() + "..."

styles = {"shout": shout, "whisper": whisper}
for name in ["shout", "whisper"]:
    print(styles[name]("Hello"))    # HELLO!  then  hello...
