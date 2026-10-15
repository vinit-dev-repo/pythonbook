# greet.py
print(f"This file's __name__ is: {__name__}")

if __name__ == "__main__":
    print("Running directly!")
else:
    print("Imported as a module.")
