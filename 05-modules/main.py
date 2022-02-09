# print() # str
# input() # str
# "".format() # str

# def my_function():
    # function body
    # return None or pass

# functia trebuie apelata dupa corpul functiei

# def your_function(x: str) -> str:
#     print("Hello", x)
#     return x
#
# name = input("Numele meu este: ")
# your_function(name)

# datetime
# data = "220229"
# import  datetime
#
# try:
#     datetime.datetime.strptime(data, "%y%m%d")
#     return True
# except ValueError:
#    return False

# def my_function(a: str, b: str, c: str = "2") -> (str, str, str): # 2 valoare default
#     return a, b, c

# print(my_function(a="1", c="2", b="3" ))
# print(my_function("1", "3", "2"))
# print(my_function("1", c="2", b="3"))
# print(my_function("3", a="1", c="2")) # nu este corect

# def my_function():
#     pass
#
# a = my_function()
# print(a)
#
# b = None
# print(type(b))


# def my_function(n):
#     if n % 2 == 0:
#         return True
#     return False
#
#
# print(my_function(3))
# nr = input("Introduceti un numar: ")
# if my_function(int(nr)) is True:
#     print("Nr este divizibil")
# elif my_function(int(nr) is False):
#     print("Nr nu este divizibil")

# global
# var = 1
# def my_function(var1):
#     global var # atribuie valoare in namespace-ul global
#     var = var1
#     return f"Cunosti aceasta variabila: {var}?"
#
#
# print(my_function(3))
# var = 1
# print(var)

# lista = [1, 2, 3, [4, 5, [6,7]]]
# print(lista[3][2][0])

# try except

# try:
#     # blok de expresii
# except:
#     # daca apare o exceptie si vrem sa afisam ceva

# try:
#     valoare = int(input("Prima cifra din CNP: "))
#     # impartire = 1 / valoare
#     lista = [1]
#     # lista.append("2")
#     valoare = lista[0.5]
# except TypeError: # putem sa scrie mai multe exceptii pe aceasi ramura
#     print("Type error")
# else:
#     print("nu exista exceptie")
# finally:
#     print("se executa oricum")
# except AttributeError:
#     print("Eroare de sintaxa")
# except ValueError:
#     print("Ai introdus gresit")
# except ZeroDivisionError:
#     print("Eroare la impartire")
# except Exception as e: # inglobeaza toate erorile
#     print("Exceptie la impartire", e)

