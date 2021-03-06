  # 1. Vehicul
# 1.1 Vehicul de apa
# 1.2 Vechiul de aer
# 1.3 Vehicul de spatiu
# 1.4 Vehicul terestru
# 1.4.1 Vehicul de teren
# 1.4.2 Vehicul de curse
# 1. este super clasa pentru 1.1 -> 1.4
# 1.1 -> 1.4 este subclasa pentru 1

# 2. Animale
# 2.1 Mamifere
# 2.1.1 Animale salbatice
# 2.1.2 Animale domestice
# 2.2 Reptile
# 2. pentru 2.1. si 2.2. este superclasa
# 2.1. si 2.2. pentru 2. sunt subclase
# 2.1.1. si 2.1.2 pentru 2.1. sunt subclase
# 2.1.1. si 2.1.2 pentru 2. sunt subclase

# Max este un caine mare care doarme toata ziua.
# obiectul -> (lucrurl care se poate schimba, un substantiv) Max
# clasa -> (notiunea generica pe baza careia se bazeaza propozitia, substantiv) caine
# proprietatea ->(cel care se modifica pe obiect, adjectivul) mare
# activitatea ->(se defineste o metoda in cadrul clasei, verb) doarme toata ziua (pate fi transformat intr-o metoda)

# Un Logan verde merge incet.
# obiectul -> Logan
# clasa -> masina
# proprietatea -> verde
# activitatea -> merge incet

# Lenovo-ul gri se poate cumpara la un pret mai mic de pe magazi online.
# obiectul -> Lenovo
# clasa -> laptop
# proprietatea -> gri
# activitatea ->  se poatecumpara

# Sa se realizeze jocul X&0 intre 2 jucator in care:
# primul jucator este mereu calculatorul
# exista reguli de joc pentru mutari
# obiectele -> calculator / omul
# clasa -> jocul
# proprietatea -> primul jucator este mereu calculatorul
# activitatea -> mutarile /calculul de scor al scorul jocului

# class MyFirstClass:
#     # init - constructor
#     pass
#
# # obiect
# object = MyFirstClass()

# Problema stivei.

# stack = []
#
# def push(val):
#     stack.append(val)
#     return stack
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
#
# print(push(3))
# print(push(2))
# print(push(1))
#
# print(pop())
# print(pop())
# print(pop())

# Problema cu OOP

# class Stack:
#     def __init__(self):
#         self.__stack_list = [] # proprietate # __ -> proprietate privata (encapsulation)
#
#     def push(self, val): # activitate (metoda)
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
#     def __str__(self):# metoda ca sa vedem elementele
#         return f"{self.__stack_list}"
#
# obiect_stiva = Stack()
# obiect_stiva.push(3)
# print(obiect_stiva)
# obiect_stiva.push(2)
# print(obiect_stiva)
# obiect_stiva.push(1)
# print(obiect_stiva)
# obiect_stiva.pop()
# obiect_stiva.pop()
# obiect_stiva.pop()

# New class
# class ClasaExemplu:
#
#     def __init__(self, val=1):
#         self.first = val
#         self.second = 0
#
#     def set_second(self, val=2):
#         self.second = val
#
#     def __str__(self):
#         return f"{self.first} {self.second}"
#
#
# obiect_1 = ClasaExemplu()
# obiect_2 = ClasaExemplu(2)
# obiect_3 = ClasaExemplu(3)

# print(obiect_1)
# print(obiect_2)
# print(obiect_3.set_second(3))
# print(obiect_3)
# print(obiect_3.second)


# class Caine:
#     nr_picioare = 4 # atribut
#     def __init__(self, name,  vaccin, age=3):# constructor - rol de a crea obiecte cu data diferite
#         self.__nume = name # proprietate privata
#         self.varsta = age
#         self.vaccinuri = vaccin
#
#         self.stare = "tanar"
#         self.cumpara = "mancare"
#         if self.varsta == 4:
#             self.stare = "batran"
#         else:
#             self.cumpara = "jucarie"
#
#         # Caine.nr_picioare = 3 # modificare la intializare atributul nr de picioare
#
#     def __str__(self):
#         return f"{self.nume} - {self.varsta}"
#
#     def change_name(self, name): #metoda
#         self.nume = name
#         return "Ceva"
#
# obiect_1 = Caine("Rex", 10, 4)
# print(type(obiect_1).__name__) # verificare nume clasa

# print(obiect_1.cumpara)
# print(hasattr(Caine, "nr_picioare")) # functie care afisiaza daca exista sau nu atributul respectiv
# print(obiect_1.__dict__) # afiseaza proprietati
# print(obiect_1._Caine__nume) # accesam proprietati private
# print(obiect_1)
# print(obiect_1.nr_picioare)
# print(obiect_1.nume)
# print(obiect_1.vaccinuri)

# validator CNP cu clase
#
# class Validator:
#     def __init__(self, CNP):
#         self.cnp = CNP
#
#     def lungime (self):
#         if len(self.cnp) != 13:
#             return False
#         return True
#
#     def __str__(self):
#         if self.lungime() is True:
#             return f"CNP-ul este {self.cnp} este valid"
#         return f"CNP-ul este {self.cnp} nu este valid"

# class Star:
#
#     def __init__(self, nume, galaxie):
#         self.name = nume
#         self.galaxy = galaxie
#
#     def __str__(self):
#         return f"{self.name} este in {self.galaxy}"
#
#
# soare = Star("Soarele", "Calea Lacteei")
# print(soare)

# vehicul
# vehiculdeteren
# vehiculdetractare

# class Vehicul:
#     pass
#
#
# class VehiculTeren(Vehicul): # scriem intre paranteze clasa mostenire
#     pass
#
#
# class VehiculTractare(VehiculTeren):
#     pass

# parinti sunt Vehicul pentru VehiculTeren si VehiculTractare (indirect)
# parinti sunt VehiculTeren pentru VechiuclTractare
# parintii sunt superclase pentru copii (superclass)
# copiii sunt VehiculTeren si VehiculTractare (indirect) pentru Vehiucl
# copilul este VehiculTractare pentru VehiculTeren
# copii se numesc subclase

# print("Vehicul VehiculTeren VehiculTractare")
# for cls1 in [Vehicul, VehiculTeren, VehiculTractare]:
#     for cls2 in [Vehicul, VehiculTeren, VehiculTractare]:
#         print(issubclass(cls1, cls2), end='\t')
#     print()

# cum verificam daca o clasa are mostenire
# vehicul1 = Vehicul()
# vehicul_teren = VehiculTeren()
# vehicul_tractare = VehiculTractare()
# print(isinstance(vehicul1, Vehicul))
# print(isinstance(vehicul1, VehiculTeren))
# print(isinstance(vehicul_teren, Vehicul))
# print(isinstance(vehicul_tractare, Vehicul))
# print(isinstance(vehicul1, VehiculTractare))
#
# for obj in [vehicul1, vehicul_teren, vehicul_tractare]:
#     for cls in [Vehicul, VehiculTeren, VehiculTractare]:
#         print(isinstance(obj, cls, end='\t'))
#     print()

# class Exemplu:
#
#     def __init__(self, val):
#         self.value = val
#
#     def __str__(self):
#         return f'{self.value}'
#
#
# obiect_1 = Exemplu(0)
# obiect_2 = Exemplu(2)
# obiect_3 = obiect_1
# obiect_3.value += 1
#
# print(obiect_1 is obiect_2)
# print(obiect_1.value, '247')
# print(obiect_2 is obiect_3)
# print(obiect_2.value, '249')
# print(obiect_3 is obiect_1)
# obiect_1.value = 7
# print(obiect_3.value, obiect_1.value, '251')
# print(obiect_1.value, obiect_2.value, obiect_3.value)

# string_1 = "Maria are mere "
# string_2 = "Maria are mere mari"
# string_1 += "mari"
# string_2 = string_1 # alternativ
#
# print(string_1 == string_2, string_1 is string_2)

# class SuperClass:
#
#     supVar = 1 # variabila de clasa
#     variabila_clasa = 6
#
#     def __init__(self, nume):
#         self.name = nume
#         # self.var_1 = 101
#
#     def __str__(self):
#         return f'Numele meste este {self.name}'
#
# class Clasa3(SuperClass):
#
#     variabila_clasa = 5
#
#     def __init__(self, nume):
#         super().__init__(nume)
#         self.name = nume
#         self.var_2 = 201
#         self.var_1 = 101
#
#     def prima_metoda(self):
#         return 4
#
# class Subclass(Clasa3):
#
#     subVar = 2 # variabila de clasa
#     supVar = 3
#
#     def __init__(self, nume):
#         self.var_1 = 202
#         print(self.var_1)
#         super().__init__(nume) # invoca constructorul superclasei + acces la toate resursele disponibile in superclasa
#         self.var_3 = 301
#         self.var_1 = 203
#         # self.name = nume
#         # Super.__init__(self, nume)
#
#     def __str__(self):
#         return f'Nume'

# obiect = Subclass("Bogdan")
# print(obiect.subVar)
# print(obiect.supVar)
# print(obiect.variabila_clasa)
# print(obiect.var_3, obiect.var_2, obiect.var_1)
# print(obiect.prima_metoda())

# Continuare 16.03.22

class A:

    def info(self):
        return 'Clasa A'

class F:

    def info(self):
        return 'Clasa F'


class B(A):
    pass
    # def info(self):
    #     return 'Clasa B'

class C(A):
    pass
    # def info(self):
    #     return 'Clasa C'


class D(A, C):
    pass


print(D().info())