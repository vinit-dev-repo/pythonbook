# ask_age.py
def ask_age():
    while True:
        try:
            return int(input("Enter your age: "))
        except ValueError:
            print("That wasn't an integer; try again")

print("Entered:", ask_age())
