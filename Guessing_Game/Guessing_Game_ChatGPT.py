import random

def greet_player():
    """Greet the player."""
    print("Welcome to the Number Guessing Game!")

def ask_to_play():
    """Ask the player if they want to play."""
    while True:
        response = input("Do you want to play? (yes/no): ").lower()
        if response in ('yes', 'no'):
            return response == 'yes'
        else:
            print("Please enter 'yes' or 'no'.")

def generate_random_number():
    """Generate a random number between 1 and 10."""
    return random.randint(1, 10)

def get_user_guess():
    """Get the player's guess and handle errors."""
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if 1 <= guess <= 10:
                return guess
            else:
                print("Please enter a number within the provided range.")
        except ValueError:
            print("Please enter a valid integer.")

def play_game():
    """Main function to play the game."""
    greet_player()
    
    best_score = float('inf')  # Initialize best score to positive infinity

    while True:
        if not ask_to_play():
            print("Goodbye!")
            break

        secret_number = generate_random_number()
        attempts = 0

        while True:
            attempts += 1
            user_guess = get_user_guess()

            if user_guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                
                if attempts < best_score:
                    best_score = attempts
                    print(f"New best score: {best_score} attempts!")
                else:
                    print(f"Current best score: {best_score} attempts.")
                    
                break
            else:
                print("Wrong guess. Try again!")

                # Provide a hint
                if user_guess < secret_number:
                    print("Hint: The number is higher.")
                else:
                    print("Hint: The number is lower.")

if __name__ == "__main__":
    play_game()
