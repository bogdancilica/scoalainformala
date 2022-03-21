# decorator - functie care este folosit ca argument la o alta functie

# def decorator_simplu(function):
#     print(f'Apelam functia {function.__name__}')
#     return function
#
# @decorator_simplu
# def functie_simpla():
#     return 'Buna seara'
#
# print(functie_simpla())

# def decorator_depozit(material):
#     def ambalaj(functia_noastra):
#         def ambalaj_intern(*args):
#             print(f'Ambalam produse din {functia_noastra.__name__} cu {material}')
#             return f'{functia_noastra.__name__} cu {material}: {", ".join(x for x in  functia_noastra(*args))}'
#             # return args
#         return ambalaj_intern
#     return ambalaj
#
# @decorator_depozit('hartie')
# def impachetare_carti(*args):
#     return args
#
# @decorator_depozit("folie alimentara")
# def impachetare_fructe(*args):
#     return args
#
# print(impachetare_carti("Amintiri din copilarie", "Baltagul"))
# print(impachetare_fructe('mere', 'pere'))

# def decorator(functie):
#     def decoreza(var):
#         return functie(var)
#     return decoreza
#
# def p(functie):
#     def decoreaza(var):
#         return f"<p>{functie(var)}</p>"
#     return decoreaza
#
# @p
# def text(sir):
#     return sir.upper()
#
#
# # text_p = decorator(text)
# print(text("Salut"))

# class Dog:
#
#     def __init__(self, nume):
#         self.__nume = nume
#
#     @property # nu mai trebuie sa apelam metoda (are setter si deleter)
#     def name(self):
#         return self.__nume
#
#     @name.setter # setam valori pe proprietatea respectiva - reatribuire de valoare pe atribut
#     def name(self, nume):
#         self.__nume = nume
#
#     @name.deleter
#     def name(self):
#         del self.__nume
#
# my_dog = Dog(nume="Rex")
# print(my_dog.name)
#
# my_dog.name = "Ben"
# print(my_dog.name)
#
# del my_dog.name
# print(my_dog.name)

# class Cat:
#
#     legs_no = 4
#
#     def __init__(self, nume):
#         self.__nume = nume
#
#
#     @property # getter
#     def name(self):
#         return self.__nume
#
#     @name.setter
#     def name(self, nume):
#         self.__nume = nume
#
#
#     @name.deleter
#     def name(self):
#         del self.__nume
#
#     def change_name(self, nume):
#         self.__nume = nume

    # def __str__(self):
    #     return f"{self.__nume}"


# cat_object = Cat("Fluffy")
# cat_object.change_name("Milly")
# print(cat_object)
# print(cat_object.name)
# cat_object.name = "Milly"
# print(cat_object.name)
# print(cat_object.legs_no) # cu properties am facut din 'name' acelasi lucru cu 'legs_no'

from datetime import date

class Persoana:

    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    @classmethod # transforma varsta ani in metoda de clasa
    def varsta_ani(cls, num1, varsta1): # trebuie sa respecte ordinea din constructor, numele nu trebuie sa fie la fel
        return cls(num1, date.today().year - varsta1)

    @staticmethod # medoda independenta a clasei : denumire clasa.metoda fara sa tina cont de constructor
    def stare(ani):
        return ani > 18

persona_1 = Persoana("Ion", 21)
print(persona_1.varsta) # 21

persona_2 = Persoana.varsta_ani("Maria", 20)
print(persona_2.varsta)

print(Persoana.stare(22))