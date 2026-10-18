class Config2:
    factor = 10
    values = [1, 2, 3]
    scaled = [v * factor for v in values]   # NameError -- factor not visible in here either
