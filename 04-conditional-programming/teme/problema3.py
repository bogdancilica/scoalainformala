# Tema Curs 4 - Conditional programming, loops and functions
# Problema 3 - Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr
# întreg, altfel returnează valoarea 0.

n = input("Check: ")
def check_int(n):
    return n if n.isnumeric() else 0


print(check_int(n))