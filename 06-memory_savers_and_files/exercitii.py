# def function(new_list: list):
#     length = len(new_list)
#     temp_list = new_list[-1]
#     new_list[0] = new_list[length - 1]
#     new_list[length - 1] = temp_list
#     return new_list
#
# param_list = [22, 11, 9, 44, 56]
# print(function(param_list))


# a = "Ana are mere"
# lista = []
# for i, e in enumerate(list(a)):
#     if i % 2 ==0:
#         lista.append(e)
# print(lista)
# scriere alterantiva
# lista = [e for i, e in enumerate(list(a)) if i % 2 == 0]

# lista = ["a", "b", "12", "cde"]
# def functie(lista: list):
#     lista = [1, 2, "abc"]
#     new_list = []
#     for i in lista:
#         new_list.append(i)
#     return new_list
#
# print(functie(lista))


# def functie(lista):
#     item = 1
#     for x, y in enumerate(lista):
#         item *= x
#         return lista[y + 1]
#
# lista = [1, 2, 3]
# print(functie(lista))


# list comprehension
# lista = []
# for item in "Ana are mere":
#     lista.append(item)
# # scriere alternative
# lista = [item for item in "Ana are mere"]
# print(lista)


# my_numbers = [1, 2, 3, 4, 5]
# lista_numere = [item ** 2 for item in my_numbers if item % 2 == 0]
# print(lista_numere)


# lista_produse = ["ciocolata", "suc", "mere", "miere", "apa"]
# lista_noua = [ x for x in lista_produse if "a" in x]
# print(lista_noua)

# lista = [x for x in range(10) if x < 5]
# print(lista)

# a, b = 10, 20
# if a < b:
#     min = a
# else:
#     min = b
#scriere alternativa - operator ternar
# min = a if a < b else b
# print(min)

# lista_produse = ["ciocolata", "suc", "mere", "miere", "apa"]
# lista_noua = [ x if x != "suc" else "apa minerala" for x in lista_produse]
# print(lista_noua)


# x = 1
#
# def f():
#     return x
#
# print(x)
# print(f())


# x = [1, 2, "hello", "world", ["another", "list"]]
# print(len(x[3]))


# x = (1, 2, 3)
# x[1] = 4
# tuple nu sunt indexabile


# a = [1, 2, 3]
# b = [4, 5]
#
# print(a + b * 3)

# x = [1, 2, 3, 4]
# print(x[-1:])

# x = [0, 1, [2]]
# x[2][0] = 3
# x[2].append(4)
# x[2] = 2
# print(x)

# def exercitiu(i):
#     for i in range(i):
#         return i
#
# x = exercitiu(3)
# print(x)

# def func(*args):
#     return 3 + len(args)
#
# print(func(4, 4, 4))
