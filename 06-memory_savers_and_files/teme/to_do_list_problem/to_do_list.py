# Tema Fisiere - To Do List - Part 1
# Se cere realizarea unui to-do list utilizând noțiunile învățate până în acest moment.

from datetime import datetime
import pandas as pd

# 1. adaugare categorii de taskuri
categorii = {
    "Categorii": []
}

nr_categorii = input("Cate categorii doriti sa introduceti?: ")
while not nr_categorii.isdigit():
    nr_categorii = input("Introduceti un numar: ")

for i in range(int(nr_categorii)):
    categorie = input("Introduceti categorie: ")
    categorii["Categorii"].append(categorie)

lista_categorii = pd.DataFrame(categorii)

# export categorii to csv
fisier = lista_categorii.to_csv("categorii.csv")

# 2. adaugare taskuri
taskuri = {
    "Nume Task": [],
    "Data Limita": [],
    "Responsabil": [],
    "Categorie": []
}

# interogare - numar de taskuri
nr_taskuri = input("Cate taskuri doriti sa introduceti?: ")
while not nr_taskuri.isdigit():
    nr_taskuri = input("Introduceti un numar: ")
print("")

# adaugare nume, data, responsabil si categorie pentru task
for i in range(int(nr_taskuri)):
    # introducere nume
    nume = input("Introduceti numele taskului: ")
    taskuri["Nume Task"].append(nume)

    # introducere data
    while True:
        data_limita = input("Introduceti termenul limita (zz.ll.aaaa oo:mm): ")
        try:
            datetime.strptime(data_limita, "%d.%m.%Y %H:%M")
            break
        except ValueError:
            print("Formatul gresit!")
    taskuri["Data Limita"].append(data_limita)

    # introducere responsabil
    responsabil = input("Introduceti un responsabil pentru task: ")
    taskuri["Responsabil"].append(responsabil)

    # introducere categorie
    categorie_task = input(f"Introduceti o categorie (categorii: {categorii['Categorii']}): ")
    while categorie_task not in categorii['Categorii']:
        categorie_task = input(f"Categorie inexistenta. Alegeti din lista: (categorii: {categorii['Categorii']}): ")
    taskuri["Categorie"].append(categorie_task)
    print("")

lista_taskuri = pd.DataFrame(taskuri)
# export taskuri to csv
fisier = lista_taskuri.to_csv("taskuri.csv")
