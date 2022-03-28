class Catalog:

    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume
        self.absente = 0
        self.materii = {}


    def __str__(self):
        return f'{self.nume} {self.prenume}: {self.absente}\n \t Materii si Note {self.materii} \n \t absente: {self.absente}'


    def increment_abs(self):
        self.absente += 1

    def delete_abs(self, numar_abs):
        if self.absente >= numar_abs:
            self.absente -= numar_abs

class Extensie1(Catalog):

    def __init__(self, nume, prenume):
        super().__init__(nume, prenume)


    def add_subject(self, materie, note):
        self.materii.update({materie: note})


    def print_all(self):
        return f'{self.materii.keys()}'


    def final_grade(self):

        note_finale = {}
        for k, v in self.materii.items():
            if all(isinstance(x, int) for x in v):
                medie = sum(v) / len(v)
                note_finale.update({k: medie})
        return note_finale



student = Catalog('Roata', 'Ion')
student.increment_abs()
student.increment_abs()
student.increment_abs()
print(student)
student.delete_abs(2)
print(student)

student2 = Catalog("Pop", "Andrei")
student2.increment_abs()
student2.increment_abs()
student2.increment_abs()
student2.increment_abs()
print(student2)
student2.delete_abs(2)
print(student2)

obj = Extensie1("Ana", "Maria")
obj.add_subject("Python", [5, 7, 9])
obj.add_subject("Math", [5, 7, 9])
print(obj.final_grade())
# print(obj.print_all())