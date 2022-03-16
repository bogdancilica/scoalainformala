class Rata:

    ochi = 2

    def __init__(self, inaltime, greutate, gen):
        self.inaltime = inaltime
        self.greutate = greutate
        self.gen = gen

    def merge(self):
        pass

    def macane(self):
        return "Mac-mac"

rata_1 = Rata(inaltime=10, greutate=3.4, gen="Feminin") # am instantiat clasa rata
rata_2 = Rata(inaltime=20, greutate=5, gen="Masculin")

print(Rata.ochi) # atributul de clasa se poate accesa prin clasa
print(rata_1.macane()) # metodele sunt comune obiectelor(rata_1, rata_2)
