# Tema Curs 3 - Data Structures

# declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).
a = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
b = sorted(a)
print(b)

# afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
c = sorted(a)[::-1]
print(c)

# afișează o listă ce conține numerele pare din lista ordonată (folosind slice)
d = b[1::2]
print(d)

# afișează o listă ce conține numerele impare din lista ordonată (folosind slice)
e = b[::2]
print(e)

# afisează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice).
f = b[2::3]
print(f)