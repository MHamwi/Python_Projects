import random

attempts_history = []

def compare_number(computer, player, attempt):
    attempt += 1

    if player > computer:
        while True:
            try:
                player = int(input('You have to guess a lower number: '))
                if not 1 <= player <= 10:
                    raise ValueError("Number must be between 1 and 10.")
                break
            except ValueError:
                print("Invalid input. Please enter an integer between 1 and 10.")

    elif player < computer:
        while True:
            try:
                player = int(input('You have to guess a higher number: '))
                if not 1 <= player <= 10:
                    raise ValueError("Number must be between 1 and 10.")
                break
            except ValueError:
                print("Invalid input. Please enter an integer between 1 and 10.")

    else:
        return attempt

    return compare_number(computer, player, attempt)

def guessing_game():
    print('Welcome back! Are you ready for some fun?')
    
    players = {'player': 0, 'computer': random.randint(1, 10)}

    user_input = input('Are you sure you want to play this game? (yes/no): ').lower()

    if user_input == 'yes':
        while user_input == 'yes':
            try:
                player_number = int(input('Guess a number between 1 and 10: '))
                if not 1 <= player_number <= 10:
                    raise ValueError("Number must be between 1 and 10.")
                players['player'] = player_number
                break
            except ValueError:
                print("Invalid input. Please enter an integer between 1 and 10.")

        final_score = compare_number(players['computer'], players['player'], 0)
        
        print(final_score)

        if final_score:
            print(f'Congratulations! It took you {final_score} attempts!')
            attempts_history.append(final_score)
            print(f'The best score is: {min(attempts_history)} attempts')

if __name__ == '__main__':
    guessing_game()
