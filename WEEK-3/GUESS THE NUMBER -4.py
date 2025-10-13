import random

print("I'm thinking of a number between 1 and 100.")
secret = random.randint(1, 100)   # pick a secret number
attempts = 0
while True:                       # repeat until the player guesses correctly
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")
    else:
        print(f"Correct! The number was {secret}. You took {attempts} tries.")
        break

    # exit the loop because the guess is correct
