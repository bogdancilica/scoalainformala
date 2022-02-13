# X si 0
# Human player vs Computer
# De asemenea, pentru alegerea unei casute libere de catre masina/robot sau de catre om aveti in vedere urmatoarele:
# intrarile sunt de la 1 la 9 astfel: 1|2|3 4|5|6 7|8|9
# pozitia 5 este cea mai vanata
# pozitia 1 sau 3 sau 7 sau 9 reprezinta optiunea a doua in cerintele unei masini.
# Prima valoare disponibila dintre acestea va fi marcata cu “O” de catre masina/robot
# In cazul in care toate acestea sunt ocupate se incearca prima valoare ramasa libera dintre 2,4,6,8

import random
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
print("Play X & 0:")


def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])
    print('')


def cine_incepe():
    intrebare = input("Vrei sa incepi tu jocul?'y/n': ")
    while intrebare not in "yn":
        intrebare = input("Alege din 'y/n': ")
    return intrebare == "y"


def alegerea_mea():
    alegere = int(input("Alege un numar de la 1 la 9: "))
    if board[alegere - 1] == " ":
        board[alegere - 1] = "X"


def alegere_calculator():
    if board[4] == " ":
        board[4] = '0'
    elif board[0] == " ":
        board[0] = '0'
    elif board[2] == " ":
        board[2] = '0'
    elif board[6] == " ":
        board[6] = '0'
    elif board[8] == " ":
        board[8] = '0'
    else:
        ramas = [1, 3, 5, 7]
        computer_choice = random.choice(ramas)
        while computer_choice not in ramas:
            board[computer_choice] = '0'


def check_castigator():
    row_1 = board[0] == board[1] == board[2] != " "
    row_2 = board[3] == board[4] == board[5] != " "
    row_3 = board[6] == board[7] == board[8] != " "
    column_1 = board[0] == board[3] == board[6] != " "
    column_2 = board[1] == board[4] == board[7] != " "
    column_3 = board[2] == board[5] == board[8] != " "
    diagonal_1 = board[0] == board[4] == board[8] != " "
    diagonal_2 = board[2] == board[4] == board[6] != " "
    if row_1 or row_2 or row_3 or column_1 or column_2 or column_3 or diagonal_1 or diagonal_2:
        return False
    else:
        return True


def cine_castiga():
    if board[0] == board[1] == board[2] == "X":
        return "Ai castigat"
    elif board[3] == board[4] == board[5] == "X":
        return "Ai castigat"
    elif board[6] == board[7] == board[8] == "X":
        return "Ai castigat"
    elif board[0] == board[3] == board[6] == "X":
        return "Ai castigat"
    elif board[1] == board[4] == board[7] == "X":
        return "Ai castigat"
    elif board[2] == board[5] == board[8] == "X":
        return "Ai castigat"
    elif board[0] == board[4] == board[8] == "X":
        return "Ai castigat"
    elif board[2] == board[4] == board[6] == "X":
        return "Ai castigat"

    elif board[0] == board[1] == board[2] == "0":
        return "Ai pierdut"
    elif board[3] == board[4] == board[5] == "0":
        return "Ai pierdut"
    elif board[6] == board[7] == board[8] == "0":
        return "Ai pierdut"
    elif board[0] == board[3] == board[6] == "0":
        return "Ai pierdut"
    elif board[1] == board[4] == board[7] == "0":
        return "Ai pierdut"
    elif board[2] == board[5] == board[8] == "0":
        return "Ai pierdut"
    elif board[0] == board[4] == board[8] == "0":
        return "Ai pierdut"
    elif board[2] == board[4] == board[6] == "0":
        return "Ai pierdut"

    else:
        return "Egalitate"


def game():
    if cine_incepe():
        while check_castigator():
            print_board()
            alegerea_mea()
            alegere_calculator()
            print_board()
        cine_castiga()
    else:
        while check_castigator():
            alegere_calculator()
            print_board()
            alegerea_mea()
            print_board()
        cine_castiga()

print(game())