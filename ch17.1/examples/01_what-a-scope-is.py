def bedroom():
    poster = "Python logo"   # only exists inside this function
    print(poster)

bedroom()
print(poster)                 # NameError — "poster" doesn't exist out here
