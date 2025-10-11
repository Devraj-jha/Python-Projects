import random

def welcome_message():
    print("=" * 50)
    print("🎯 Welcome to the Number Guessing Game!")
    print("=" * 50)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")
    print()

def get_valid_guess():
    while True:
        guess = input("Enter your guess: ")
        if guess.isdigit():
            return int(guess)
        else:
            print("Invalid input. Please enter a number between 1 and 100.")

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = None

    while guess != secret_number:
        guess = get_valid_guess()
        attempts += 1

        if guess < secret_number:
            print("🔻 Too low! Try again.\n")
        elif guess > secret_number:
            print("🔺 Too high! Try again.\n")
        else:
            print(f" Correct! You guessed the number in {attempts} attempts.\n")

def play_again():
    while True:
        again = input("Would you like to play again? (yes/no): ").lower()
        if again in ('yes', 'y'):
            return True
        elif again in ('no', 'n'):
            print("Thanks for playing! Goodbye 👋")
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def main():
    welcome_message()
    while True:
        play_game()
        if not play_again():
            break

if __name__ == "__main__":
    main()
