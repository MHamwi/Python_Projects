import random
from game_options import Options  # Assuming you have a 'game_options' module with the 'Options' class

def validate_user_input(user_input):
    """
    Validates user input for game options.

    Parameters:
    - user_input (Options): User-selected game option.

    Returns:
    - bool: True if the user input is valid, False otherwise.
    """
    return user_input.opt in ['paper', 'scissor', 'rock']

def each_round(Blue_Player, Red_Player):
    """
    Simulates a round of the game between two players.

    Parameters:
    - Blue_Player (Options): Option chosen by the Blue player.
    - Red_Player (Options): Option chosen by the Red player.

    Returns:
    - str: Result of the round ('tie', 'blue is win', 'red is win').
    """
    print(f'Blue_Player chose: {Blue_Player.opt}')
    print(f'Red_Player chose: {Red_Player.opt}')

    if Blue_Player.opt == Red_Player.opt:
        return 'tie'
    elif Blue_Player.opt == Red_Player.enemy:
        return 'blue is win'
    else:
        return 'red is win'

def play_game():
    """
    Plays the Paper, Scissor, Rock game.
    """
    print('Welcome to Paper, Scissor, Rock Game! ')
    
    while True:
        number_of_rounds = int(input('Enter the number of rounds you would like to play (enter 0 to exit): '))
        
        if number_of_rounds == 0:
            print('Thank you for playing! See you soon!')
            break

        enemy = input("Choose the mode of play: against computer (c) or against human (h)").lower()
        
        options = [Options('paper'), Options('scissor'), Options('rock')]
        
        players_scores = {'Blue_Score': 0, 'Red_Score': 0}
        
        print('Rules of the game:\nEach player chooses one option: paper, scissor, or rock\n'
              'Paper beats the rock, rock beats the scissor, scissor beats the paper\n'
              'Every time a player wins, their score increases by one point. ')
        print('-----------------The Game is Started-----------------')

        for current_round in range(number_of_rounds):
            if enemy == "human" or enemy == "h":
                Blue_Player = Options(input('Blue_Player, choose your option: paper, scissor, or rock').lower())
                while not validate_user_input(Blue_Player):
                    Blue_Player = Options(input('OPS! You chose an unsupported option.\n'
                                                'Choose your option: paper, scissor, or rock').lower())

                Red_Player = Options(input('Red_Player, choose your option: paper, scissor, or rock').lower())
                while not validate_user_input(Red_Player):
                    Red_Player = Options(input('OPS! You chose an unsupported option.\n'
                                               'Choose your option: paper, scissor, or rock').lower())
            elif enemy == "computer" or enemy == 'c':
                Blue_Player = Options(input('Blue_Player, choose your option: paper, scissor, or rock').lower())
                while not validate_user_input(Blue_Player):
                    Blue_Player = Options(input('OPS! You chose an unsupported option.\n'
                                                'Choose your option: paper, scissor, or rock').lower())

                Red_Player = random.choice(options)
                print(f"Red_Player chose: {Red_Player.opt}")
            else:
                print("Sorry, your enemy is not supported yet :P")
                break

            result = each_round(Blue_Player, Red_Player)

            players_scores['Blue_Score'] += 1 if result == "blue is win" else 0
            players_scores['Red_Score'] += 1 if result == "red is win" else 0

            print(f"Blue's score: {players_scores['Blue_Score']}, Red's score: {players_scores['Red_Score']}")
        
        print('Game Over!')
        print(f"Final Score - Blue: {players_scores['Blue_Score']}, Red: {players_scores['Red_Score']}")
        
        if players_scores['Blue_Score'] > players_scores['Red_Score']:
            print("------Blue Wins!------")
        elif players_scores['Red_Score'] > players_scores['Blue_Score']:
            print("------Red Wins!------")
        else:
            print("------It's a Tie!------")

if __name__ == "__main__":
    play_game()
