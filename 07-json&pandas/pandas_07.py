import pandas as pd

# dictionar_date = {
#     "masini": ['Dacia', 'Volvo', 'Renalut'],
#     "culoare": ['rosu', 'alb', 'verde']
# }
#
# variabila = pd.DataFrame(dictionar_date)
# print(variabila)

# masini = ['Dacia', 'Volvo', 'Renalut']
# variabila = pd.Series(masini)
# print(variabila)
# print(variabila[0])
#
# variabila = pd.Series(masini, index = ["x", "y", "z"])
# print(variabila)
# print(variabila["y"])
# print(variabila[0]) # functioneaza si cu intex


# masini = {"x": "Dacia", "y": "Volvo", "z": "Renault"}
# variabila = pd.Series(masini)
# print(variabila)
#
# variabila = pd.Series(masini, index = ["y", "z"])
# print(variabila)


# dictionar_date = {
#     "masini": ['Dacia', 'Volvo', 'Renalut'],
#     "culoare": ['rosu', 'alb', 'verde']
# }

# variabila = pd.DataFrame(dictionar_date)
# print(variabila)
# print(variabila.loc[0])
# print(variabila.loc[[0, 1]])

# variabila = pd.DataFrame(dictionar_date, index=["producator1", "producator2", "producator3"])
# print(variabila)
# print(variabila.loc["producator1"])
# print(variabila.loc[["producator1", "producator2"]])

# data = {
#   "producator 1": {
#     "masina": "Dacia",
#     "culoare": "rosu"
#   },
#     "producator 2": {
#     "masina": "Volvo",
#     "culoare": "alb"
#   },
#     "producator 3": {
#     "masina": "Renault",
#     "culoare": "verde"
#   }
# }

# variabila1 = pd.DataFrame(data)
variabila1 = pd.read_json('data.json')
# print(variabila1)

# ssl error
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#
# url = 'https://api.exchangerate-api.com/v4/latest/USD'
# variabila1 = pd.read_json(url)
# print(variabila1)

# export in excel
fisier = variabila1.to_csv("data.csv")
