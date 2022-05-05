#  Creati un program ce are o clasa numita util. Clasa are o variabila a clasei de tip lista
# populata automat in constructor(__init__) cu obiectul.
# Creati a doua clasa numita izatori care primeste in constructor doua argumente numite
# user si passw, formand cu ajutorul acestora doua atribute cu acelasi nume.
# Creati a treia clasa numita utilizatori care sa mosteneasca clasele util și izatori fără a
# pierde din functionalitatea claselor mostenite.
# De asemenea, aceasta clasa are o metoda privata numita parole care sa returneze un
# set cu toate parolele și o metoda privata numita useri care sa returneze un set cu toți
# userii. Se va folosi variabila clasei de tip lista care are toate obiectele pentru căutare.
# Interpretorul trebuie sa ridice o eroare setata de voi în cazul în care este apelat
# obiectul prin len(). Setati 3 obiecte și testați functionalitatea

class EroarePersonala(Exception):
    def __init__(self, cod, mesaj):
        super(EroarePersonala, self).__init__(str(cod)+'=>'+str(mesaj))

class Util():

    lista = []
    def __init__(self):
        Utilizatori.lista.append(self)
        self.lista.append(self)

class Izatori:

    def __init__(self, user, passw):
        self.user = user
        self.passw = passw

class Utilizatori(Util, Izatori):

    def __init__(self, user, passw):
        Util.__init__(self)
        Izatori.__init__(self, user, passw)

    def __useri(self):
        return set([e.user for e in self.lista])

    def __parole(self):
        return set([e.passw for e in self.lista])

    @staticmethod
    def __len__(self):
        raise EroarePersonala(101, "Ai gresit apelarea!")



obj1 = Utilizatori("bogdan", "pass")
obj2 = Utilizatori("florin", "pass")
obj3 = Utilizatori("raul", "pass")

print(obj1._Utilizatori__useri())
print(obj1._Utilizatori__parole())

try:
    len(obj1)
except(Exception) as e:
    print(e)




