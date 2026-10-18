class Light:
    def __init__(self, is_on):
        self.is_on = is_on

    def __bool__(self):
        return self.is_on

lamp = Light(is_on=False)
if lamp:
    print("Room is lit")
else:
    print("Room is dark")
