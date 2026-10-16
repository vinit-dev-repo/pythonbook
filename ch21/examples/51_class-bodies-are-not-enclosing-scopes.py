class Config:
    factor = 10

    def scale(self, n):
        return n * self.factor   # go through self

c = Config()
print(c.scale(5))
