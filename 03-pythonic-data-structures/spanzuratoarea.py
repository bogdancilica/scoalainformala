# reguli
# daca primul caracter si ultimul se repetau in cuvand,caracterul trebuia afisat
# restul caracterelor erau ascunse
# 7 sanse de a ghici cuvantul
# o _ o _ _ _ o _ e e
word = "onomataopee"

lista_cuvant = []
for iterator in word:
    lista_cuvant.append('_')
    if iterator == word[0] or iterator == word[-1]:
        lista_cuvant[-1] = iterator
print(" ".join(lista_cuvant))
numar_incercari = 1
lista_litere_incercate = set()
while numar_incercari <= 7:
    litera = input("Alege o litera: ")
    if litera in word.lower():
        for index, valoare in enumerate(word):
            if valoare.lower() == litera:
                lista_cuvant[index] = litera
    else:
        if litera not in lista_litere_incercate:
            numar_incercari += 1
        lista_litere_incercate.add(litera)
        print(f"Litera nu exista, deja ai incercat urmatoarele litere {','.join(lista_litere_incercate)}")
        print(f"Mai ai {7 - numar_incercari} incercari")

    if 9 - int(numar_incercari) == 0:
        print(f"Ai pierdut! Cuvantul ere {word}")
    elif "". join(lista_cuvant) == word:
        print("Ai castigat!")
        break
    else:
        print(" ".join(lista_cuvant))


