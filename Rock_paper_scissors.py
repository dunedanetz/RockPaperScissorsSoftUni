import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

if player_move == 'r':
    player_move = rock
elif player_move == 'p':
    player_move = paper
elif player_move == 's':
    player_move = scissors
else:
    raise SystemExit('Invalid input. Try again...')


computer_move = random.choice([rock, paper, scissors])
if player_move == rock and computer_move == scissors or \
        player_move == paper and computer_move == rock or \
        player_move == scissors and computer_move == paper:
    print("You win!")
    if computer_move == rock:
        print(f'The computer chose {rock}')
    if computer_move == paper:
        print(f'The computer chose {paper}')
    if computer_move == scissors:
        print(f'The computer chose {scissors}')
elif computer_move == player_move:
    print("Draw!")
    if computer_move == rock:
        print(f'The computer chose {rock}')
    if computer_move == paper:
        print(f'The computer chose {paper}')
    if computer_move == scissors:
        print(f'The computer chose {scissors}')
else:
    print('You lose!')
    if computer_move == rock:
        print(f'The computer chose {rock}')
    if computer_move == paper:
        print(f'The computer chose {paper}')
    if computer_move == scissors:
        print(f'The computer chose {scissors}')
