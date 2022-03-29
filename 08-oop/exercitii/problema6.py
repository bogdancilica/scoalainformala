class Util:
    lista_obj = []
    def __init__(self):
        self.lista = []

    # metoda de adaugat la o lista
    # def add_subject(self, obj):
    #     self.lista.append(obj)

class Izatori:

    def __init__(self, user, passw):
        self.user = user
        self.passw = passw

class Utilizatori(Util, Izatori):

    def __init__(self, user, passw):
        Util.__init__(self)
        Izatori.__init__(self, user, passw)


    def parole(self):
        self.__parole.add(self.__parole)

