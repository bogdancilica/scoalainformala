# VALIDATOR CNP
# Codul numeric personal sau CNP este codul unic al fiecărei persoane născute în România, format din exact 13 cifre.
# Format: S AA LL ZZ JJ NNN C.
# S reprezintă sexul și secolul în care s-a născut persoana care posedă acel CNP.
    # Prima cifră a CNP-ului este: (sex bărbătesc / sex femeiesc)
    # 1 / 2 - născuți între 1 ianuarie 1900 și 31 decembrie 1999
    # 3 / 4 - născuți între 1 ianuarie 1800 și 31 decembrie 1899
    # 5 / 6 - născuți între 1 ianuarie 2000 și 31 decembrie 2099
    # 7 / 8 - pentru persoanele străine rezidente în România.
    # În plus 9 - pentru persoanele străine.
# AA LL ZZ reprezinda data nasterii
    # AA este un număr format din 2 cifre și reprezintă ultimele 2 cifre din anul nașterii.
    # LL este un număr format din 2 cifre și reprezintă luna nașterii persoanei.
    # ZZ reprezintă ziua nașterii în format de 2 cifre. Pentru zilele de la 1 la 9 se adaugă 0 înaintea datei.
# JJ este un număr format din două cifre și este reprezentat de codul județului sau sectorului
# în care s-a născut persoana ori în care avea domiciliul sau reședința în momentul acordării C.N.P.
# NNN este un număr format din 3 cifre din intervalul 001 - 999.
# C este cifră de control (un cod autodetector) aflată în relație cu toate celelate 12 cifre ale CNP-ului.

from datetime import datetime

cnp = input("Introduceti CNP: ")

incercari = 3
while incercari != 0:
    if len(cnp) != 13 or not cnp.isdigit():
        cnp = input(f"Ati introdus gresit! CNP are 13 cifre. Mai aveti {incercari} incercari: ")
    else:
        break
    incercari -= 1


def sex():
    return int(cnp[0]) in range(1, 10)


def data_nasterii():
    try:
        datetime.strptime(cnp[1:7], "%y%m%d")
        return True
    except ValueError:
        return False


def judet():
    return cnp[7:9] in ["%02d" % i for i in range(1, 47)] or int(cnp[7:9]) in [51, 52]


def nnn():
    return cnp[9:12] in ["%03d" % i for i in range(1, 1000)]


def cifra_de_control():
    n = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)
    suma = 0
    for i, j in zip(cnp[:12], n):
        suma += int(i) * j
    a = suma % 11
    if a == 10:
        c = 1
    else:
        c = a
    return int(cnp[12]) == c


def validare():
    if not cnp.isdigit():
        return "\nAti introdus un CNP invalid."
    elif sex() and data_nasterii() and judet() and nnn() and cifra_de_control():
        return "\nAti introdus un CNP valid."
    else:
        return "\nAti introdus un CNP invalid."


print(validare())
