from random import choice

# 1. Ask for player name
player_name = input('Introdu numele: ')
# 2. Greet and show playing options
print('Welcome: `Rock - Paper - Scissors` ')

game_on = True
while game_on:

    # 3. Player is asked to make a choice (read from the console)
    comp_choice = None
    user_choice = None
    while comp_choice == user_choice:
        user_choice = input('Chose from: "R/P/S"').lower()
        optiuni = ['r', 'p', 's']
        while user_choice not in optiuni:
            user_choice = input('Chose from: "R/P/S"').lower()
        # 4. Computer makes a random choice
        print('Egalitate se alege din nou! \n')

        comp_choice = choice(optiuni)
        print(comp_choice)
        # 5. If computer makes the same choice, play again

    print(f'Computer choice was: {comp_choice}')
    print(f'{player_name} choice was {user_choice}')
    if user_choice == 'r':
        if comp_choice == 'p':
            print(f'You lost!')
        else:
            print('You won!')
    elif user_choice == 'p':
        if comp_choice == 's':
            print(f'You lost!')
        else:
            print('You won!')
    else:
        if comp_choice == 'r':
            print("You lost!")
        else:
            print('You won')
    game_status = input('Do yo wanna play more? y/n ')
    while game_status not in 'yn':
        game_status = input('Do yo wanna play more? y/n ')
    if game_status != 'y':
        game_on = False


# 6. If not, show the result
# 7. Ask player if he/she wants to play again
# 8. Game stops when the player decides not to play again