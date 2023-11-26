import random

def greet_player():
    """Display a welcome message to the player."""
    print("Welcome to the Guess the Number game!")

def get_player_choice():
    """Ask the player if they want to play the game."""
    while True:
        choice = input("Do you want to play? (yes/no): ").lower()
        if choice in ['yes', 'no']:
            return choice
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

def generate_random_number():
    """Generate a random number between 1 and 10."""
    return random.randint(1, 10)

def get_player_guess():
    """Prompt the player to guess a number between 1 and 10."""
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if 1 <= guess <= 10:
                return guess
            else:
                print("Invalid guess. Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def congrats_and_attempts(attempts):
    """Display a congratulatory message along with the number of attempts."""
    print(f"Congratulations! You guessed the number. It took you {attempts} attempts.")

def play_game():
    """Main function to orchestrate the game."""
    greet_player()

    choice = get_player_choice()

    if choice == 'yes':
        print("Great! Let's get started.")
        target_number = generate_random_number()
        attempts = guess_number(target_number, 0)
        congrats_and_attempts(attempts)
    elif choice == 'no':
        print("Maybe next time. Goodbye!")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        play_game()

def guess_number(target_number, attempts):
    """Recursive function to guess the number."""
    player_guess = get_player_guess()

    if player_guess == target_number:
        return attempts + 1
    else:
        print("Try again. Wrong guess!")
        return guess_number(target_number, attempts + 1)

if __name__ == "__main__":
    play_game()
