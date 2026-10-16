number = 64
guess = number / 2
for step in range(7):
    guess = (guess + number / guess) / 2
    print("step", step + 1, "guess", guess)
