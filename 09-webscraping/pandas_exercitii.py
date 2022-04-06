import pandas as pd
# print(pd.__version__)


# a = {'x': 1, 'y': 7, 'z': 2}
# variabila = pd.Series(a, index=a.keys())
# variabila = pd.Series(a, index=['x', 'y']) # printeaza doar index x si y
# print(variabila)


# data = {
#     'key1': [0, 1, 2],
#     'key2': [3, 4, 5]
#  } # data frame

# variabila1 = pd.DataFrame(data)
# variabila1 = pd.DataFrame(data, index=['linie1', 'linie2', 'linie3'])
# print(variabila1)

#acesare valori key 2, coloana
# print(variabila1['key2'])

# acesare linia 2
# print(variabila1.loc['linie2'])


# open csv

df = pd.read_csv('EXEMPLU.csv')
# print(df)

#salvare valori in csv
# transforamre json (data) in data frame
# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }
#
# df = pd.DataFrame(data)
# print(df)

df = pd.read_csv('test.csv')
# print(df)

#stergere b

# for x in df.index:
#   print(df.loc[x, 'AL'])
#   if df.loc[x, 'AL'] == ':':
#     df.drop(x, inplace= True)
# print(df)
#
# df1 = df.to_csv('test1.csv')

# corelare date
# print(df.corr())

# statistici descriptive
# print(df.describe())

#media
# print(df.mean())


# grafic cu date
# import matplotlib.pyplot as plt
# df.plot(kind='scatter', x='AT', y='BE')
# plt.show()

# histograma
# df['AT'].plot(kind = 'hist')
# plt.show()

# afisare primele linii
# print(df.head(2))

# afisare ultimele linii
# print(df.tail(3))


# pastrare doar randurile fara None
# new_df = df.dropna(inplace=True)
# print(df)

#inlocuire None
# print(df.fillna(0))

# inlocuine None pe o anumita coloana
# df['AL'].fillna(0, inplace=True)
# print(df)

# inlocuire o valoare specifica
# df.loc[7, 'AL'] = 45
# print(df)

# inlocuire simbol

# df.replace(': ', 0, inplace=True)# folosim inplace  sau realocam la o alta variabila
# df.replace(':', 0, inplace=True)
# print(df)

# trimitere set de date catre csv
# df.to_csv('test1.csv')

# intoarcere table
# print(df.transpose())
