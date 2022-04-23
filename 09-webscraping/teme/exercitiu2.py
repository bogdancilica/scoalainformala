import pandas as pd
# 1) se cere realizarea unei functii get_year_data() care sa contina 2 param:
# Setul de date si anul pentru care se doreste preluarea datelor get_year_data(dataset, "2019") returneaza
# {'2019': [('Romania', 84), ('Germany', 95), ..., ('Latvia', 85)]}
# 2) se cere realizarea unei functii get_country_data(dataset, "Romania"), care sa contina 2 param.
# datasetul si tara pentru care se doreste primirea datelor.
# ex: get_country_data(dataset, "Romania") returneaza
# {'Romania': [('2019', 84), ('2018', 86), ..., ('2011', 72)]}
# 3) de asemenea, se cere realizarea unei functii perform_average(country_data['Romania']) care sa returneze
# media per tara, ex perform_average(country_data['Romania']) returneaza 79.4


description = ('Country', ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])

dataset = [
 ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
 ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ','89 ', '90 ']),
 ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ','72 ']),
 ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ','87 ', '90 ']),
 ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ','72 ', '75 ']),
 ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 b', ': ','96 ']),
 ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ','86 ', '90 ']),
 ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ','86 ', '87 ']),
 ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ','94 ', '95 ']),
 ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ','93 ', '95 ']),
 ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ','89 ', '90 ']),
 ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ','90 ', '90 ']),
 ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ','76 ', '79 ']),
 ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ','86 ', '91 ']),
 ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ','94 ', '94 ']),
 ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ','89 ', '90 ']),
 ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ','82 ', '81 ']),
 ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ','83 ', '86 ']),
 ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ','89 ', '91 ']),
 ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99', '98 ']),
 ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ','84 ', '85 ']),
 ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ','78 ', '82 ']),
 ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ','93 b', '95 ']),
 ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 b', '79 ','82 ', '85 ']),
 ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ','74 ']),
 ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79', '82 ']),
 ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ','84 ', '86 ']),
 ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ','98 ', '98 ']),
 ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ','96 ', '98 ']),
 ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ','84 ', '87 ']),
 ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ','79 ', '81 ']),
 ('RO', ['47 ', '54 ', '58 ', '61 b', '68 ', '72 ', '76 ','81 ', '84 ']),
 ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ','80 ']),
 ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 b', '95 ','93 ', '96 ']),
 ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ','87 ', '89 ']),
 ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ','81 ', '82 ']),
 ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84', '88 ']),
 ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ','95 ', '96 ']),
 ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ','93 ']),
]

def get_year_data(data, an):
    lista1 = []
    for country in data:
        lista1.append((country[0], country[1][description[1].index(an)]))
    return {an: lista1}


def get_country_data(data, tara):
    lista2 = []
    for country in data:
        if country[0] == tara:
            for i in range(9):
                lista2.append((description[1][i], country[1][i]))
    return {tara: lista2[::-1]}


def perform_average(tara):
    pass

# print(get_year_data(dataset, "2019"))
# print(get_country_data(dataset, "RO"))

# Structura 1 - conform cerintei
# structura datelor trebuie sa fie ca in exemplul de mai jos, pentru o preluare rapida:
# {
#  'Romania': [
#  {
#  'year': '2019',
#  'coverage': 84
#  }, {
#  'year': '2018',
#  'coverage': 67
#  },
# ..., {
#  'year': '2011',
#  'coverage': 72
#  }
#  ],

data = {}
for country in dataset:
    lista = []
    for i in range(9):
        lista.append({
            'year': description[1][::-1][i],
            'coverage': int(country[1][::-1][i][:2].strip()) if country[1][::-1][i][:2].strip().isdigit() else 0
        })
    data[country[0]] = lista

df = pd.DataFrame(data)
df1 = df.to_csv('exercitiu2_v1.csv')

# Structura 2

data1 = {}
for country in dataset:
    lista = []
    for i in range(9):
        lista.append(int(country[1][::-1][i][:2].strip()) if country[1][::-1][i][:2].strip().isdigit() else 0)
    data1[country[0]] = lista

df2 = pd.DataFrame(data1, index=['2019', '2018', '2017', '2014', '2015', '2014', '2013', '2012', '2011'])
df3 = df2.transpose()
df4 = df3.to_csv('exercitiu2_v2.csv')

# 3. Calculati media pe fiecare tara pe care sa o adaugati ca si ultima coloana in tabelul format mai sus

df3['Medie'] = df3.mean(axis=1)
df3.to_csv('exercitiu2_v2.csv')

# 4. Afisati informatii referitoare la date cu ajutorul  functiei describe
# print(df2.describe())

# 5. Realizati un grafic de tip scatter pentru primele 2 tari in functie de media acestora
import matplotlib.pyplot as plt
# df2.plot(kind='scatter', x='AL', y='AT')
# plt.show()

# 6. Realizati o histograma a datelor pentru Romania.
# df2['RO'].plot(kind = 'hist')
# plt.show()