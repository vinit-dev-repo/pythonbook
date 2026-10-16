class Config:
    factor = 10

    def scale(self, n):
        return n * factor   # NameError -- factor is not visible in here

c = Config()
print(c.scale(5))
