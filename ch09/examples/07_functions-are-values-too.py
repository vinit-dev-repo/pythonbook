def shout(text):
    return text.upper() + "!"

def whisper(text):
    return text.lower() + "..."

def announce(text, style_function):
    print(style_function(text))

announce("hello there", shout)
announce("hello there", whisper)
