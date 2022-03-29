# 2. Scrie un program care sa elimine si sa printeze numerele din 3 in 3 pana cand lista devine goala. (1 punct)
# Lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def elimina_num(lista):
    position = 2
    index = 0
    len_lista = len(lista)
    while len_lista > 0:
        index = (position + index) % len_lista
        print(lista.pop(index))
        print(lista)
        len_lista -= 1


numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
elimina_num(numere)
