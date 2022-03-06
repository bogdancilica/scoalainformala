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
# 3.Filtrare date: filtrarea datelor reprezintă o listare a datelor în funcție de anumite detalii date de la tastatură.
# se cere de la tastatură câmpul după care se realizeaza filtrarea:
# criteriile de filtrare sunt:
# 3.1. Task
# 3.2. Dată
# 3.3. Persoană responsabilă
# 3.4. Categorie
# - după alegerea campului de la tastatură se cere introducerea unui string utilizat pentru filtrarea în lista inițială,
# astfel încât din lista inițială să rămână doar datele care conțin / încep cu valoarea introdusă
# - se afișează lista rămasă
# 4. Adăugarea unui nou task în lista inițială
# 5. Editarea detaliilor referitoare la task, dată, persoană sau categorie dintr-un anumit task ales de utilizator
# de la tastatură (când se cere această opțiune, se va lista lista de taskuri cu un identificator unic pe rand,
# astfel încât să se știe ce informație urmează să editeze utilizatorul)
# 6. Ștergerea unui task din lista inițială.

import pandas as pd
from datetime import datetime

df = pd.read_csv('taskuri.csv', index_col=0)
print("Meniu operatii")

# creare meniu
# while - da posibilitatea utilizatorului sa sa faca operatii consecutive in meniu
intrebare = "y"
while intrebare == "y":
    print("""
    1. Listare date (sortare în funcție de categorie)
    2. Sortare date
    3. Filtrare date
    4. Adaugare task
    5. Editare task
    6. Stergere task
    """)
    meniu = input("Alegeti o optiune de mai sus (1, 2, 3, 4, 5, 6): ")
    while meniu not in "123456":
        meniu = input("Nu ati ales din lista. Mai incercati (1, 2, 3, 4, 5, 6): ")
    print(" ")

    # listare initiala de date (sortare in functie de categorie)
    if meniu == "1":
        df = pd.read_csv('taskuri.csv', index_col=0)
        df1 = df.sort_values("Categorie")
        df1.to_csv('taskuri.csv')
        print(df1)

    # sortare date
    if meniu == "2":
        print("""
    1. sortare ascendentă task
    2. sortare descendentă task
    3. sortare ascendentă data
    4. sortare descendentă data
    5. sortare ascendentă persoana responsabilă
    6. sortare descendentă persoană responsabilă
    7. sortare ascendentă categorie
    8. sortare descendentă categorie
        """)
        meniu_2 = input("Ati ales optiunea 2. Alegeti sub-optiunea din lista de mai sus (1, 2, 3, 4, 5, 6, 7, 8): ")
        while meniu_2 not in "12345678":
            meniu_2 = input("Nu ati ales din lista. Mai incercati (1, 2, 3, 4, 5, 6, 7, 8): ")
        if meniu_2 == "1":
            df21 = df.sort_values("Nume Task")
            df21.to_csv('taskuri.csv')
            print(df21)
        elif meniu_2 == "2":
            df22 = df.sort_values("Nume Task", ascending=False)
            df22.to_csv('taskuri.csv')
            print(df22)
        elif meniu_2 == "3":
            df23 = df.sort_values("Data Limita")
            df23.to_csv('taskuri.csv')
            print(df23)
        elif meniu_2 == "4":
            df24 = df.sort_values("Data Limita", ascending=False)
            df24.to_csv('taskuri.csv')
            print(df24)
        elif meniu_2 == "5":
            df25 = df.sort_values("Responsabil")
            df25.to_csv('taskuri.csv')
            print(df25)
        elif meniu_2 == "6":
            df26 = df.sort_values("Responsabil", ascending=False)
            df26.to_csv('taskuri.csv')
            print(df26)
        elif meniu_2 == "7":
            df27 = df.sort_values("Categorie")
            df27.to_csv('taskuri.csv')
            print(df27)
        else:
            df28 = df.sort_values("Categorie", ascending=False)
            df28.to_csv('taskuri.csv')
            print(df28)

    # filtrare date
    if meniu == "3":
        df = pd.read_csv('taskuri.csv', index_col=0)
        print("Lista actuala: ")
        print(df)
        print("""
    1. filtrare dupa task
    2. filtrare dupa data
    3. filtrare dupa persoana responsabilă
    4. filtrare dupa categorie
        """)
        meniu_3 = input("Ati ales optiunea 3. Alegeti sub-optiunea din lista de mai sus (1, 2, 3, 4): ")
        while meniu_3 not in "1234":
            meniu_3 = input("Nu ati ales din lista. Mai incercati (1, 2, 3, 4): ")

        string_filtrare = input("Introduceti un string dupa care se va realiza filtrarea: ")

        if meniu_3 == "1":
            print(df[df["Nume Task"].str.contains(string_filtrare)])
        elif meniu_3 == "2":
            print(df[df["Data Limita"].str.contains(string_filtrare)])
        elif meniu_3 == "3":
            print(df[df["Responsabil"].str.contains(string_filtrare)])
        else:
            print(df[df["Categorie"].str.contains(string_filtrare)])

    # adaugare task
    if meniu == "4":
        df = pd.read_csv('taskuri.csv', index_col=0)
        print("Lista actuala: ")
        print(df)
        print("Task nou")

        # introducere nume
        nume = input("Introduceti numele taskului: ")
        while nume in df["Nume Task"].to_list():
            nume = input("Taskul exista deja in lista. Incercati din nou: ")

        # introducere data
        while True:
            data_limita = input("Introduceti termenul limita (aaaa.ll.zz oo:mm): ")
            try:
                datetime.strptime(data_limita, "%Y.%m.%d %H:%M")
                break
            except ValueError:
                print("Formatul gresit!")

        # introducere responsabil
        responsabil = input("Introduceti un responsabil pentru task: ")

        # introducere categorie
        categorie_task = input(f"Introduceti o categorie (categorii: {set(df['Categorie'].to_list())}): ")
        while categorie_task not in df['Categorie'].to_list():
            categorie_task = input(f"Categorie inexistenta. Alegeti din lista: (categorii: {set(df['Categorie'].to_list())}): ")

        new_row = {"Nume Task": nume, "Data Limita": data_limita, "Responsabil":  responsabil,"Categorie": categorie_task}

        print("Lista noua: ")
        df4 = df.append(new_row, ignore_index=True)
        df4.to_csv('taskuri.csv')
        print(df4)

    # editare task
    if meniu == "5":
        df = pd.read_csv('taskuri.csv', index_col=0)
        df.sort_index(inplace=True)
        print(df)

        index_task = int(input("Ce task doriti sa editati?(index din lista de mai sus): "))
        while index_task not in df.index.to_list():
            index_task = int(input("Index gresit! (index din lista de mai sus): "))

        print("""
    1. editare nume task
    2. editare data limita
    3. editare responsabil
    4. editare categorie
        """)
        meniu_5 = input("Alegeti tipul de editare din lista de mai sus (1, 2, 3, 4): ")
        while meniu_5 not in "1234":
            meniu_5 = input("Nu ati ales din lista. Mai incercati (1, 2, 3, 4): ")

        if meniu_5 == "1":
            # schimbare nume
            nume = input("Introduceti noul nume al taskului: ")
            while nume in df["Nume Task"].to_list():
                nume = input("Taskul exista deja in lista. Incercati din nou: ")

            df.at[index_task, "Nume Task"] = nume
            df.to_csv('taskuri.csv')
            print("\nLista dupa editare: ")
            print(df)

        elif meniu_5 == "2":
            # introducere data noua
            while True:
                data_limita = input("Introduceti noul termen limita (aaaa.ll.zz oo:mm): ")
                try:
                    datetime.strptime(data_limita, "%Y.%m.%d %H:%M")
                    break
                except ValueError:
                    print("Formatul gresit!")

            df.at[index_task, "Data Limita"] = data_limita
            df.to_csv('taskuri.csv')
            print("\nLista dupa editare: ")
            print(df)

        elif meniu_5 == "3":
            # introducere responsabil nou
            responsabil = input("Introduceti noul responsabil pentru task: ")

            df.at[index_task, "Responsabil"] = responsabil
            df.to_csv('taskuri.csv')
            print("\nLista dupa editare: ")
            print(df)

        elif meniu_5 == "4":
            # introducere categorie noua
            categorie_task = input(f"Introduceti o categorie noua (categorii: {set(df['Categorie'].to_list())}): ")
            while categorie_task not in df['Categorie'].to_list():
                categorie_task = input(
                    f"Categorie inexistenta. Alegeti din lista: (categorii: {set(df['Categorie'].to_list())}): ")

            df.at[index_task, "Categorie"] = categorie_task
            df.to_csv('taskuri.csv')
            print("\nLista dupa editare: ")
            print(df)

    # stergere task
    if meniu == "6":
        df = pd.read_csv('taskuri.csv', index_col=0)
        df.sort_index(inplace=True)
        print(df)

        index_task = int(input("Ce task doriti sa stergeti?(index din lista de mai sus): "))
        while index_task not in df.index.to_list():
            index_task = int(input("Index gresit! (index din lista de mai sus): "))

        df6 = df.drop(index_task)
        df6 = df6.reset_index(drop=True)
        df6.to_csv('taskuri.csv')
        print("\nLista dupa stergere: ")
        print(df6)

    print(" ")
    intrebare = input("Doriti sa continuati (y/n): ")
    while intrebare not in "yn":
        intrebare = input("Alege y(Yes) or n(No): ")

