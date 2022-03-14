class ClasaMea:

    gamma = 0 # variabila de clasa

    def __init__(self): # constructor - initializeaza valorile dintr-un obiect
        self.alpha = 1 # variabila de instanta (definita in constructor)
        self.__delta = 3 # variabila de instanta privata


obj = ClasaMea() # instantierea clasei ClasaMea, definire obiect
obj.beta = 2 # variabila de instanta care exista doar in interiorul obiectului
print(obj.__dict__) # dictionar cu obiectele clasei
print(obj.alpha)
print(obj.gamma)
print(ClasaMea.gamma) # accesare alterantive gamma
print(obj._ClasaMea__delta) # accesare delta