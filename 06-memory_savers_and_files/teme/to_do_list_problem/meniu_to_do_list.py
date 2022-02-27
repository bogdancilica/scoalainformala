# Nota: Inca nu este finalizat.

# Tema Fisiere - To Do List - Part 2
# Meniu To Do List
# cerinte suplimentare: meniu pentru utilizator cu urmatoarele operatii
# 1. Listare date în afișarea inițială a datelor se realizează o sortare în funcție de categorie.
# 2. Sortare: se alege o opțiune din cele 8 de mai jos:
# 2.1. sortare ascendentă task
# 2.2. sortare descendentă task
# 2.3. sortare ascendentă data
# 2.4. sortare descendentă data
# 2.5. sortare ascendentă persoana responsabilă
# 2.6. sortare descendentă persoană responsabilă
# 2.7. sortare ascendentă categorie
# 2.8. sortare descendentă categorie
#3.Filtrare date: filtrarea datelor reprezintă de fapt o listare a datelor în funcție de anumite detalii date de la tastatură.
# se cere de la tastatură câmpul după care se realizeaza filtrarea:
# criteriile de filtrare sunt:
# 3.1. Task
# 3.2. Dată
# 3.3. Persoană responsabilă
# 3.4. Categorie
# - după alegerea campului de la tastatură se cere introducerea unui string utilizat pentru filtrarea în lista inițială de date,
# astfel încât din lista inițială să rămână doar datele care conțin / încep cu valoarea introdusă
# - se afișează lista rămasă
# 4. Adăugarea unui nou task în lista inițială
# 5. Editarea detaliilor referitoare la task, dată, persoană sau categorie dintr-un anumit task ales de utilizator de la tastatură
# (când se cere această opțiune, se va lista lista de taskuri cu un identificator unic pe rand, astfel încât să se știe ce informație urmează să editeze utilizatorul)
# 6. Ștergerea unui task din lista inițială.

import csv
import pandas as pd

lista_taskuri = pd.read_csv('taskuri.csv', index_col=0)

# creare meniu
print("""
1. Listare date (sortare în funcție de categorie)
2. Sortare
3. Filtrare date
4. Adaugare task
5. Editare task
6. Stergere task
""")
meniu = input("Alegeti o optiune de mai sus (1, 2, 3, 4, 5, 6): ")
while meniu not in "123456":
    meniu = input("Nu ati ales din lista. Mai incercati (1, 2, 3, 4, 5, 6): ")
#
if meniu == "1":
    print(lista_taskuri)


#TODO: "2. Sortare 3. Filtrare date 4. Adaugare task 5. Editare task 6. Stergere task"

# if meniu == "2":
#     print("""
#     # 1. sortare ascendentă task
#     # 2. sortare descendentă task
#     # 3. sortare ascendentă data
#     # 4. sortare descendentă data
#     # 5. sortare ascendentă persoana responsabilă
#     # 6. sortare descendentă persoană responsabilă
#     # 7. sortare ascendentă categorie
#     # 8. sortare descendentă categorie
#     """)
#     meniu_2 = input("Ati ales optiunea 2. Alegeti sub-optiunea din lista de mai sus (1, 2, 3, 4, 5, 6, 7, 8): ")
#     while meniu_2 not in "12345678":
#         meniu_2 = input("Nu ati ales din lista. Mai incercati (1, 2, 3, 4, 5, 6, 7, 8): ")