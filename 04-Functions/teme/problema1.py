# Tema Curs 4 - Conditional programming, loops and functions
# Problema 1 - Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze
# suma parametrilor care reprezintă numere întregi sau reale.

def my_function(*args, **kwargs):
    suma = 0
    for number in args:
        if isinstance(number, (int, float)):
            suma += number
    return suma


# test
print(my_function(1, 5, -3, "abc", [12, 56, "cad"]))
print(my_function())
print(my_function(2, 4, "abc", param_1=2))
