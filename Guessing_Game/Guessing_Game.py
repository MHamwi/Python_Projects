import random

from numpy import integer
attempts_history= []
attempt = 0

def compare_number(computer,player,attempt):
    attempt+=1
    if player > computer:
        while True:
            try:
                player= int(input(f'you have to guess lower number: '))
                if player > 10 or player < 1:
                    raise ValueError
                break
            except ValueError:
                print('Invalid number, you must guess a number between 1 and 10')
    elif player < computer:
        while True:
            try:
                player = int(input(f'you have to guess higher number: '))
                if player > 10 or player< 1:
                    raise ValueError
                break
            except ValueError:
                print('Invalid number, you must guess a number between 1 and 10')
    else:
        return attempt
    return compare_number(computer,player, attempt)


def guessing_game():
    print('welcome back, are you ready for hitting some heads?!')
    players={'player':int,'computer':random.randint(1,10)}
    #print(players)
    while True:
        try:
            user_input = input('are you sure that, do you want to playing this horror game? (yes/no): ').lower()
            if user_input != 'yes' and user_input != 'no':
                raise ValueError
            else:
                break
        except ValueError:
                print('Invalid input, you must chose one of these valid options: yes or no')
    if user_input == 'yes':
        try:
            player_number = int(input('guess a number between 1 to 10: '))
            players['player']= player_number
            if player_number > 10 or player_number < 1:
                raise ValueError
        except ValueError:
            print('you have to guess an integer number between 1 to 10')  
    while user_input =='yes':
        final_score = compare_number(players['computer'],players['player'], attempt)
        #print(final_score)
        if final_score :
            print(f'Congratulations! it took from you {final_score} attempts!')
            attempts_history.append(final_score)
            print(f'the best score is: {min(attempts_history)} attempts')
            user_input = 'no'
        guessing_game()
                
if __name__=='__main__':
    guessing_game()