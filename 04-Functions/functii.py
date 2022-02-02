# print("Mesaj")
# format()
# control B for spec function

# def functia_mea(param_1):
#     pass

def suma(a: int, b: int = 1, c: int = 0) -> (int, int):
    """
    :param a: first param
    :param b: second param
    :param c: third param
    :return: sum if param, dif o param
    """
    return a + b + c, a - b - c  # returnam suma si diferenta

# partea de documentatie 3 X " + enter
# c cu valoare default // incepant cu python 3.8 - se poate declara paramentru cu tip de data
# -> selectam tipul datelor de iesire

variabila_1 = 1
variabila_2 = 2
sum, dif = suma(a = variabila_1, b = variabila_2)
print(sum, dif)
