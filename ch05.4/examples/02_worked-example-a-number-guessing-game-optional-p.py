import random

secret_number = random.randint(1, 10)
guesses_used = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    guesses_used = guesses_used + 1

    if guess == secret_number:
        print(f"Correct! It took you {guesses_used} guesses.")
        break
    elif guess < secret_number:
        print("Too low — try again.")
    else:
        print("Too high — try again.")
