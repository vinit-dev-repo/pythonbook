class Cat(Animal):
    @override
    def mak_sound(self):      # misspelled — Python runs this fine, no error here
        return "Meow"          # but mypy/pyright flags it: no method named mak_sound on Animal

print(Cat().mak_sound())
