import random
from game_options import Options
# first of all, run the game
# Enter the number or rounds
# ask the uer to chose the mode of playing (against computer or with friend)
# set initial score for each player
# ask player 1 to select one option
# ask player 2 to select one option or if the player 2 is computer assign its option randomly
# update the score for each player
# update current round number
# loop again untill the current round number is greater than the numbers of rounds
# Display the final score for each player
# Define the winner
run = True
options = [Options('paper'),
           Options('scissor'),
           Options('rock'),
           ]
def validate_user_input(user_input):
    if user_input.opt == 'paper' or user_input.opt == 'scissor' or user_input.opt == 'rock':
        return True
    else:
        return False
def eachRound_2players (round_number):
    round_result={'blue_score':0,'red_score':0}      
    print(f'Round {round_number}')
    blue_option = Options(input('chose your option: paper, scissor or rock').lower())
    if validate_user_input(blue_option) == False:
        blue_option = Options(input('OPS!, you chosed unsupported  option\nchose your option: paper, scissor or rock').lower())
    red_option = Options(input('chose your option: paper, scissor or rock').lower())
    if validate_user_input(red_option) == False:
        red_option = Options(input('OPS!, you chosed unsupported  option\nchose your option: paper, scissor or rock').lower())
    if blue_option.opt == red_option.opt:
        return 'tie'
    elif blue_option.opt == red_option.enemy:
        return 'blue is win'
    else:
        return 'red is win'

def eachRound_1player (round_number):  
    print(f'Round {round_number}')
    blue_option = Options(input('chose your option: paper, scissor or rock').lower())
    if validate_user_input(blue_option) == False:
        blue_option = Options(input('OPS!, you chosed unsupported  option\nchose your option: paper, scissor or rock').lower())
    red_option = random.choice(options)
    print(f"Computer option is: {red_option.opt}")
    if blue_option.opt == red_option.opt:
        return 'tie'
    elif blue_option.opt == red_option.enemy:
        return 'blue is win'
    else:
        return 'red is win'
    
while run :
    players_scores={'Blue_Score':0, "Red_Score":0}
    print('Welcome to Paper, Scissor, Rock Game, we hope you like it ')
    numberOfRounds = int(input('Please enter numbers of rounds that you would like to play or enter 0 to exit '))
    if numberOfRounds == 0:
        print('Thank you for being part of our game, see you soon! ')
        break
    enemy = input("please chose which mode you would like to  play: against computer(c) or against human (h)").lower()
    print('the rules of the game are:\neach player have to chose one of these options: paper, scissor, rock\n'
          'paper eat the rock, rock break the scissor, scissor cut the paper\n'
          'every time player win his socer increased by one point. ')
    print('-----------------The Game is Started-----------------')
    if (enemy == "human") or (enemy == "h"):
        for currentRound in range (0,numberOfRounds):
            round_result = eachRound_2players(currentRound) #result for the current round
            players_scores['Blue_Score'] += 1 if round_result == "blue is win" else 0
            players_scores['Red_Score'] += 1 if round_result == "red is win" else 0
            currentRound+= 1
            print(players_scores)
        print(f"Blue's score: {players_scores['Blue_Score']}\n"
              f"Red's score: {players_scores['Red_Score']}")
        if players_scores['Blue_Score']> players_scores['Red_Score']: 
            print("------Blue Win!------")
        elif players_scores['Blue_Score']< players_scores['Red_Score']:
            print("------Red Win!------")
        else:
            print("------It is Tie!------")
    elif enemy == "computer" or enemy == 'c':
        for currentRound in range (0,numberOfRounds):
            round_result = eachRound_1player(currentRound) #result for the current round
            players_scores['Blue_Score'] += 1 if round_result == "blue is win" else 0
            players_scores['Red_Score'] += 1 if round_result == "red is win" else 0
            currentRound+= 1
            print(players_scores)

        print(f"Blue's score: {players_scores['Blue_Score']},"
             f"\nRed's score: {players_scores['Red_Score']}")
        if players_scores['Blue_Score']> players_scores['Red_Score']: 
            print("------Blue Win!------")
        elif players_scores['Red_Score']< players_scores['Blue_Score']:
            print("------Red Win!------")
        else:
            print("------It is Tie!------")
    else:
        print("Sorry, your enemy is not supported yet :P")