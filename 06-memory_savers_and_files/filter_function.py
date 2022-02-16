lista_numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def functie_nr_pare(number):
#     if number % 2 == 0:
#         return True
#     return False
#
# iterator_numere_mare = filter(functie_nr_pare, lista_numere)
#
# print(list(iterator_numere_mare))


litere = ["a", "b", "c ", "d", "e", "i", "j"]
def filter_vocale(letter):
    vocale = ["a", "e", "i", "o", "u"]
    return True if letter in vocale else False

filtrare_vocale = filter(filter_vocale, litere)
print(list(filtrare_vocale))