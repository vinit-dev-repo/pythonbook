from collections import ChainMap

defaults = {"theme": "light", "font_size": 12, "language": "en"}
config_file = {"font_size": 14}
command_line = {"theme": "dark"}

settings = ChainMap(command_line, config_file, defaults)

print(settings["theme"])       # from command_line — checked first
print(settings["font_size"])   # from config_file — command_line didn't have it
print(settings["language"])    # from defaults — neither other map had it
