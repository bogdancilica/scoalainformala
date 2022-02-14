# map - inlocuieste pe rand elementele dintr-o lista intr-o functie
# def adunare(n):
#     return n + n


lista_numere = [1, 2, 3, 4]
lista_numere_2 = [5, 6, 7, 8]
# rezultat = map(adunare, lista_numere)
# print(list(rezultat))

# sau cu lambda in loc de functie
# rezultat = map(lambda n : n + n, lista_numere)
# print(list(rezultat))


# suma 2 liste
# rezultat = map(lambda n, m: n + m, lista_numere, lista_numere_2)
# print(list(rezultat))

# mai sus este alternativa la codul de mai jos
# def adunare(lista_numere, lista_numere_2):
#     suma = 0
#     lista_adunare = []

    # for  i in range(0, min(len(lista_numere), len(lista_numere_2)))
    #    lista_adunare.append(lista_numere[i] + lista_numere_2[i])

#     for i, v in enumerate(lista_numere):
#         for j, w in enumerate(lista_numere_2):
#             suma = v + w
#             if i == j:
#                 lista_adunare.append(suma)
#
#     return lista_adunare
#
# print(adunare(lista_numere, lista_numere_2))