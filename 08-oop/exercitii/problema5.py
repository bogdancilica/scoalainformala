class ListaCDDVD:

    lista_obj = []

    def __init__(self, titlu, continut):
        self.titlu = titlu
        self.continut = continut
        self.lista_obj.append([self.titlu, self.continut])

    @staticmethod
    def search(text):
        mesaj = "Obiectul nu a fost gasit"
        for i in ListaCDDVD.lista_obj:
            if text in i[0] or text in i[1]:
                mesaj = f'Obiectule cautat este Titlu: {i[0]}, Continut: {i[1]}'
        return mesaj


    def __str__(self):
        return f'Titlul este: {self.titlu}'

obj1 = ListaCDDVD("Titlu1", "Continut1")
obj2 = ListaCDDVD("Titlu2", "Continut2")
obj3 = ListaCDDVD("Titlu3", "Continut3")

print(obj1)
print(obj2)
print(obj3)
print(ListaCDDVD.search("Continut2"))


