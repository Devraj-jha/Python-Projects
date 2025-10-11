# I'm thinking of a number between 1 and 100.
# Can you guess what it is?

# Enter your guess: 50
# Too low!

# Enter your guess: 75
# Too high!

# Enter your guess: 63
# Correct! You guessed it in 3 tries.

import random

# Generate random number between 1 and 100
secret_number = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100.")
guess = None
attempts = 0

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {attempts} tries.")
