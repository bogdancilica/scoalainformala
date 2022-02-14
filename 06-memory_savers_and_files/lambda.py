# lambda
# my_lambda = lambda  x, y: x + y
# denumire_functie = lambda param1, param2: corp functie
# my_sum = my_lambda(2, 3)
# print(my_sum)

# mai sus alternativa la:
# def my_lambda(x, y):
#     return x + y

# diferenta
# diferenta = lambda x, y: x - y
# dif = diferenta(4, 3)
# print(dif)

# ordorare dictionare din lista in functie de paramentrul varsta
players = [{
    "first_name": "Ion",
    "last_name": "Gheorghe",
    "varsta": 12
},
{
    "first_name": "Andreea",
    "last_name": "Popa",
    "varsta": 35
},
{
    "first_name": "Isabela",
    "last_name": "Enache",
    "varsta": 25
}
]

jucator_sortati = sorted(players, key=lambda jucator: jucator["varsta"])
print(jucator_sortati)