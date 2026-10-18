shared = []
get_saved = lambda saved=shared: saved
shared.append("new")
print(get_saved())
shared = []
print(get_saved())
