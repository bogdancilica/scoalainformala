# class MyFirstClass:
#
#     pass
#
# my_first_object = MyFirstClass()

# class Caine:
#     nr_picioare = 4 # atribut
#     def __init__(self, name, age):# constructor - rol de a crea obiecte cu data diferite
#         self.nume = name
#         self.varsta = age
#
#     def __str__(self):
#         return f"{self.nume} - {self.varsta}"
#
#     def change_name(self, name): #metoda
#         self.nume = name

# print(Caine.nr_picioare)

# cainele_meu = Caine("Rex", "2")
# print(cainele_meu.nume)
# print(cainele_meu.change_name("Ben"))
# print(cainele_meu)
# print(cainele_meu.varsta)

# problema calculator cu Class

class Calculator:

    def __init__(self, op1, op2, operation): # constructor
        self.operator1 = op1
        self.operator2 = op2
        self.operatie = operation

    def adunare(self):
        return self.operator1 + self.operator2

    def scadere(self):
        return self.operator1 - self.operator2

    def __str__(self):
        if self.operatie == "+":
            return f"{self.adunare()}"
        elif self.operatie == "-":
            return f"{self.scadere()}"
# adunarea si scaderea sunt actiuni ale calculatorului

obiect1 = Calculator(1, 2, "+")
obiect2 = Calculator(1, 2, "-")
print(obiect1, obiect2)


def suma(a, b):
    return a + b

var1 = suma(1,2)
var2 = suma(3,2)