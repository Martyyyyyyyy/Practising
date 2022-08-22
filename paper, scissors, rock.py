import random

# a little fun game vs computer
def get_choices():
    player_choice = input('Enter your choice(paper, scissors, rock): ')
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)   
    choices = {'player': player_choice, 'computer': computer_choice}
    return choices

def check_win(player, computer):
    print(f'You choose: {player}, computer choose: {computer}')
    if player == 'paper' and computer == 'rock':
        print('Congrats, you win!')
    elif player == 'paper' and computer == 'scissors':
        print('Sorry, computer wins.')
    elif player == 'rock' and computer == 'paper':
        print('Sorry, computer wins.')
    elif player == 'rock' and computer == 'scissors':
        print('Congrats, you win!')
    elif player == 'scissors' and computer == 'paper':
        print('Congrats, you win!')
    elif player == 'scissors' and computer == 'rock':
        print('Sorry, computer wins.')
    else:
        print("It's a tie!")


response = get_choices()
iswin = check_win(response['player'], response['computer'])