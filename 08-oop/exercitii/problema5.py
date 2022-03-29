class ListaCDDVD:

    def __init__(self, titlu, continut):
        self.titlu = titlu
        self.continut = continut


    def search(self, text):
        if text in lista:
            return f'{self.titlu}, {self.continut}'
        return "Obiect inexistent"


    def __str__(self):
        return f'{self.titlu}'

obj1 = ListaCDDVD("Titlu1", "Continut1")
obj2 = ListaCDDVD("Titlu2", "Continut2")
obj3 = ListaCDDVD("Titlu3", "Continut3")

lista = [obj1, obj2, obj3]

print(obj1)
print(obj2)
print(obj3)


