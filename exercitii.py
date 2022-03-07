# 1. Realizati o functie care sa inlocuiasca textul din variabila string aflat
# intre valorile “start” si “end” cu textul din “text”.
# string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be
# introduced."
# # [start, end, text]
# patches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]
# Textual rezultat este: The Conquistator must meet King on top of Palace
# battlements to be introduced.
# Numaratoarea de start si end incepe cu indexul 1. Se pot introduce de la
# tastatura alte valori pentru index si text, cat si un numar mai mare de liste.
# Optimizati codul.

# string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
#
# def functie(start: int, end: int, text: str):
#     global string
#     new = string.replace(string[start - 1: end], text)
#     string = new
#     return string
#
#
# functie(5, 14, "Conquiztador")
# functie(26, 31, "King")
# functie(43, 49, "Palace")
# print(string)
# print('The Conquistator must meet King on top of Palace battlements to be introduced.')

# Problema 2

# lista_nume = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria', 'Claudiu']
# # 1. Sortati lista dupa nume
# print(sorted(lista_nume))
# # 2. Determinati numarul de aparitii al fiecarui nume
# counts = dict()
# for i in lista_nume:
#     counts[i] = counts.get(i, 0) + 1
# print(counts)

# 3. Listati numele care apare de cele mai multe ori in lista initiala.

# 4. Listati numele care apare de cele mai putine ori in lista initiala.
# print(max(counts, key=counts.get))
# print(min(counts, key=counts.get))

# min_no = min(counts.values())
# max_no = max(counts.values())
# lista_min = []
# lista_max = []
# for i in counts:
#     if counts[i] == min_no:
#         lista_min.append(i)
#     if counts[i] == max_no:
#         lista_max.append(i)
#
# print(lista_min)
# print(lista_max)

# Problema 3
# 3. Sa se verifice daca doua stringuri sunt anagrame

# def anagrame(string1, string2):
#     if sorted(string1) == sorted(string2):
#         return True
#     return False
#
# print(anagrame("tare", "rate"))
# print(anagrame("tard", "rate"))

# 4. Sa se elimine toate duplicatele dintr-o lista
# def duplicat(lista):
#     return list(dict.fromkeys(lista))
#
#
# print(duplicat(["a", "b", "c", "a", "b", "d", "c"]))

# 5. Sa se verifice daca un string este palindrom
# def palindrom(string):
#     if string == string[::-1]:
#         return True
#     return False
#
# print(palindrom("anana"))
# print(palindrom("asdadas"))

# 6. Sa se verifice ce numere lipsesc dintr-un interval
#
# def functie(start: int, end: int):
#     return list(range(start+1, end))
#
# print(functie(5, 12))

# 7. Sa se afiseze inversul unul string
# def invers(string):
#     return string[::-1]
#
# print(invers("Astazi"))

# 8. Sa se afiseze toate permutarile dintr-un string


# from itertools import permutations
# def functie(string):
#     return [''.join(p) for p in permutations(string)]
#
# print(functie("2635"))

# alternativ - but no
# def generatePermutation(string, start, end):
#     current = 0
#     # Prints the permutations
#     if (start == end - 1):
#         print(string)
#     else:
#         for current in range(start, end):
#             # Swapping the string by fixing a character
#             x = list(string)
#             temp = x[start]
#             x[start] = x[current]
#             x[current] = temp
#
#             # Recursively calling function generatePermutation() for rest of the characters
#             generatePermutation("".join(x), start + 1, end)
#             # Swapping the string by fixing a character
#             temp = x[start]
#             x[start] = x[current]
#             x[current] = temp
#
#
# str = "123"
# n = len(str)
# print("All the permutations of the string are: ")
# generatePermutation(str, 0, n)


