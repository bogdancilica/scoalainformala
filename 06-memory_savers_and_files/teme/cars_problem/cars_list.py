# Să se scrie un program care gestionează o listă de mașini. O mașină este reprezentată ca dicționar și conține
# următoarele chei: id(identificator unic), brand, model, hp, price
# Catalogare
# 1. Mașinile sunt catalogate în funcție de numărul de cai putere astfel:
# slow_cars - mașinile cu numărul de cai putere < 120.
# fast_cars - mașinile cu numărul de cai putere ≥ 120, dar < 180
# sport_cars - mașinile cu numărul de cai putere ≥ 180.
# 2. Mașinile sunt catalogate în funcție de preț astfel:
# cheap - mașinile cu prețul < 1000
# medium - mașinile cu prețul ≥ 1000, dar < 5000
# expensive - mașinile cu prețul ≥ 5000.

import csv
# import json
import pandas as pd

dictionar_masini = {
    "brand": ['Citroen', 'Volkswagen', 'BMW', 'Mercedes', 'Rolls-Royce'],
    "model": ['C4 Picasso', 'Golf', 'X1', "CLS", "Phantom"],
    "hp": [90, 110, 190, 160, 200],
    "price": [800, 2500, 4800, 4500, 8000]
}

masini = pd.DataFrame(dictionar_masini)
# export variabila 'masini' in fisierul input.csv
fisier = masini.to_csv("input.csv")

# Să se scrie un program care conține următoarele funcționalități:

# 1. citește datele de intrare dintr-un fișier aflat în fișierul input.csv
with open("input.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter=",")
    for row in csv_reader:
        print(row)

# 2. generează un folder output_data care va conține următoarele fișiere .json:
# import os
# os.mkdir("output_data")

# slow_cars.json - conține datele despre toate mașinile care se încadrează în categoria slow_cars.
a = []
for i in range(len(masini)):
    if masini.loc[i][2] < 120:
        a.append(i)
masini.loc[a].to_json("output_data\\slow_cars.json")

# fast_cars.json - conține datele despre toate mașinile care se încadrează în categoria fast_cars.
b = []
for i in range(len(masini)):
    if masini.loc[i][2] in range(120, 181):
        b.append(i)
masini.loc[b].to_json("output_data\\fast_cars.json")

# sport_cars.json - conține datele despre toate mașinile care se încadrează în categoria sport_cars.
c = []
for i in range(len(masini)):
    if masini.loc[i][2] > 180:
        c.append(i)
masini.loc[c].to_json("output_data\\sport_cars.json")

# cheap_cars.json - conține datele despre toate mașinile care se încadrează în categoria cheap.
d = []
for i in range(len(masini)):
    if masini.loc[i][3] < 1000:
        d.append(i)
masini.loc[d].to_json("output_data\\cheap_cars.json")

# medium_cars.json - conține datele despre toate mașinile care se încadrează în categoria medium.
e = []
for i in range(len(masini)):
    if masini.loc[i][3] in range(1000, 5001):
        e.append(i)
masini.loc[e].to_json("output_data\\medium_cars.json")

# expensive_cars.json - conține datele despre toate mașinile care se încadrează în categoria expensive.
f = []
for i in range(len(masini)):
    if masini.loc[i][3] > 5000:
        f.append(i)
masini.loc[f].to_json("output_data\\expensive_cars.json")

# câte un fișier care conține toate datele despre un anumit brand de mașină
g = []
for i in range(len(masini)):
    g.append(i)
    masini.loc[g].to_json(f"output_data\\{masini.loc[i][0]}.json")
    g = []
