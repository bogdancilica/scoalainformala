# X si 0
# Human Player vs Computer
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
print("Play X & 0\n")
print("Cum sa alegi pozitia: ")
print("1 | 2 | 3")
print("4 | 5 | 6")
print("7 | 8 | 9\n")


def print_board():
    print("")
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
    alegere = input("Alege un numar de la 1 la 9: ")
    valid = False
    while not valid:
        while alegere not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            alegere = input("Alege un numar de la 1 la 9: ")
        alegere = int(alegere)
        if board[alegere - 1] == " ":
            valid = True
        else:
            print("Nu poti alege acolo, Mai incearca!")
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
        while len(ramas) > 0:
            computer_choice = random.choice(ramas)
            if board[computer_choice] == " ":
                board[computer_choice] = '0'
                break
            else:
                ramas.remove(computer_choice)


def check_castigator():
    row_1 = board[0] == board[1] == board[2] != " "
    row_2 = board[3] == board[4] == board[5] != " "
    row_3 = board[6] == board[7] == board[8] != " "
    column_1 = board[0] == board[3] == board[6] != " "
    column_2 = board[1] == board[4] == board[7] != " "
    column_3 = board[2] == board[5] == board[8] != " "
    diagonal_1 = board[0] == board[4] == board[8] != " "
    diagonal_2 = board[2] == board[4] == board[6] != " "
    egalitate = " " not in board
    if row_1 or row_2 or row_3 or column_1 or column_2 or column_3 or diagonal_1 or diagonal_2 or egalitate:
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
        print(cine_castiga())

    else:
        while check_castigator():
            alegere_calculator()
            print_board()
            alegerea_mea()
        print_board()
        print(cine_castiga())


game()
