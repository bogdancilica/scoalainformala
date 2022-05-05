# Creati o clasa care sa calculeze si sa returneze operatia matematica de mai jos pentru
# 4 numere: [a(b+3)/c]*d.
# Clasa trebuie sa aiba 2 metode: prima metoda este metoda speciala init.
# Iar cea dea doua metoda este metoda speciala str.
# Va rog sa aplicati cel putin doua exemple (doua obiecte).
# Metoda init trebuie sa foloseasca parametrii default a=1,b=2,c=3,d=4 si trebuie sa suprime
# orice eroare.
# La aparitia unei erori trebuie sa afiseze textul: <>
# Folositi clasa in trei exemple:
# • cu patru parametrii numerici diferiti de cei default
# • cu 3 parametrii non-numerici
# • cu 2 parametrii numerici


class Calcul:
    def __init__(self, a=1, b=2, c=3, d=4):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def verificare(self):
        self.e = "Introduceti cifre"
        if str(self.a).isnumeric() and str(self.b).isnumeric() and str(self.c).isnumeric() and str(self.d).isnumeric():
            self.e = (self.a*(self.b+3)/self.c)*self.d
        return  self.e


    def __str__(self):
        return f'Rezultatul este: {self.verificare()}'


obj1 = Calcul()
print(obj1)

obj2 = Calcul(b=4, d=10, c=8)
print(obj2)

obj3= Calcul("x", "y", "z", d=6)
print(obj3)

obiect4 = Calcul(9,2)
print(obiect4)
