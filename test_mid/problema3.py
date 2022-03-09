# 3. Scrie un program care sa afiseze toate combinarile de 2 litere dintre valorile dictionarului de mai jos:
from itertools import permutations
lista_valori_unice = []


def combinari(dictt):
    for i in dictt:
        if len(dictt[i]) == 1:
            lista_valori_unice.append(dictt[i])
    return [''.join(p) for p in permutations(lista_valori_unice, 2)]


dictionar = {"1": "abc", "2": "s", "3": "o", "4": "n", "5": "lm", "6": "jk", "7": "gi", "8": "def", "9": "abc"}
print(combinari(dictionar))
