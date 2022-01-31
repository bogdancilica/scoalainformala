import random

intrebare = input('Vrei sa incepi tu jocul? "y/n" ')

lista = [None, None, None,
         None, None, None,
         None, None, None]
if intrebare == 'y':
    valoare_utilizator = int(input("Zi-mi un numar de la 1 la 9! "))
    if lista[valoare_utilizator - 1] is None:
        lista[valoare_utilizator - 1] = 'X'

while None in lista:

    if lista[4] is None:
        lista[4] = '0'
    elif lista[0] is None:
        lista[0] = '0'
    elif lista[2] is None:
        lista[2] = '0'
    elif lista[6] is None:
        lista[6] = '0'
    elif lista[8] is None:
        lista[8] = '0'
    else:
        ramas = [1, 3, 5, 7]
        computer_choice = random.choice(ramas)
        while computer_choice not in ramas:
            lista[computer_choice] = '0'

    # print(f"{lista[0]}   {lista[1]}   {lista[2]}\n"
    #       f"{lista[3]}   {lista[4]}   {lista[5]}\n"
    #       f"{lista[6]}   {lista[7]}   {lista[8]}")

    print(" {}     {}   {} \n {}   {}     {} \n {}  {}   {}".
          format(lista[0], lista[1], lista[2], lista[3],
                 lista[4], lista[5], lista[6], lista[7], lista[8]))


    valoare_utilizator = int(input("Zi-mi un numar de la 1 la 9! "))
    if lista[valoare_utilizator - 1] is None:
        lista[valoare_utilizator - 1] = 'X'
    # print(lista)
    if lista[0] == lista[1] == lista[2] is not None:
        if lista[0] == 'X':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[3] == lista[4] == lista[5] is not None:
        if lista[3] == 'X':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[6] == lista[7] == lista[8] is not None:
        if lista[6] == 'X':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[0] == lista[3] == lista[6] is not None:
        if lista[0] == 'X':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[1] == lista[4] == lista[7] is not None:
        if lista[1] == 'X':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[2] == lista[5] == lista[8] is not None:
        if lista[2] == 'X':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[0] == lista[4] == lista[8] is not None:
        if lista[0] == 'X':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[2] == lista[4] == lista[6] is not None:
        if lista[2] == 'X':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')