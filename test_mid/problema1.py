# 1. Scrie un program care sa calculeze suma dintre trei numere. Daca valorile sunt egale, returnati de trei ori suma acestora.(1 punct)
def suma(a: int, b: int, c: int) -> int:
    if a == b == c:
        return 3 * (a + b + c)
    return a + b + c


print(suma(7, 7, 7))
print(suma(3, 4, 5))
