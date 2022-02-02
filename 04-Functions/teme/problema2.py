# Tema Curs 4 - Conditional programming, loops and functions
# Problema 2 - Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:

# suma tuturor numerelor de la [0, n]
def get_sum(n):
    if n == 0:
        return 0
    return n + get_sum(n - 1)


# suma numerelor pare de la [0, n]
def sum_even(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return sum_even(n - 1)
    else:
        return n + sum_even(n - 1)


# suma numerelor impare de la [0. n]
def sum_odd(n):
    if n == 0:
        return 0
    if not n % 2 != 0:
        return sum_odd(n - 1)
    else:
        return n + sum_odd(n - 1)


# test
print(get_sum(3))
print(sum_even(5))
print(sum_odd(7))