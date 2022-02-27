# # Tema Fisiere
# # Se cere realizarea unui to-do list utilizând noțiunile învățate până în acest moment.
# # adaugare categorii de taskuri
# import csv
# from datetime import datetime
#
# categorii = [["CATEGORII"]]
#
# nr_categorii = input("Cate categorii doriti sa introduceti?: ")
# while not nr_categorii.isdigit():
#     nr_categorii = input("Introduceti un numar: ")
#
# for i in range(int(nr_categorii)):
#     categorie = input("Introduceti categorie: ")
#     categorii.append([categorie])
#
# with open("categorii.csv", "a", newline="") as file:
#     writer = csv.writer(file)
#     for i in categorii:
#         writer.writerow(i)
#
# # introducere task cu data limita, responsabil si categorie
# task = [["NUME", "DATA LIMITA", "RESPOSABIL", "CATEGORIE"]]
#
# nr_taskuri = input("Cate taskuri doriti sa introduceti?: ")
# while not nr_taskuri.isdigit():
#     nr_taskuri = input("Introduceti un numar: ")
# print("")
#
# # adaugare liste goale in task in functie de numarul de taskuri
# for i in range(int(nr_taskuri)):
#     task.append([])
#
# for i in range(int(nr_taskuri)):
#     nume = input("Introduceti numele taskului: ")
#     task[i + 1].append(nume)
#
#     while True:
#         data_limita = input("Introduceti termenul limita (zz.ll.aaaa oo:mm): ")
#         try:
#             datetime.strptime(data_limita, "%d.%m.%Y %H:%M")
#             break
#         except ValueError:
#             print("Formatul gresit!")
#     task[i + 1].append(data_limita)
#
#
#     responsabil = input("Introduceti un responsabil pentru task: ")
#     task[i + 1].append(responsabil)
#
#     categorie_task = input(f"Introduceti o categorie (categorii: {[categorii[categorii.index(i)][0] for i in categorii[1:]]}): ")
#     while categorie_task not in [categorii[categorii.index(i)][0] for i in categorii[1:]]:
#         categorie_task = input(f"Categorie inexistenta. Alegeti din lista: (categorii: {[categorii[categorii.index(i)][0] for i in categorii[1:]]}): ")
#     task[i + 1].append(categorie_task)
#     print("")
#
# with open("taskuri.csv", "a", newline="") as file_taskuri:
#     writer = csv.writer(file_taskuri)
#     for i in task:
#         writer.writerow(i)

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

if meniu == "1":
    with open("taskuri.csv", "r", newline="") as file_meniu:
        reader = csv.reader(file_meniu)
        for row in reader:
            print(row)

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