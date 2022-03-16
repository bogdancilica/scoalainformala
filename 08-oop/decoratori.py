# decorator - functie care este folosit ca argument la o alta functie

# def decorator_simplu(function):
#     print(f'Apelam functia {function.__name__}')
#     return function
#
# @decorator_simplu
# def functie_simpla():
#     return 'Buna seara'
#
# print(functie_simpla())

def decorator_depozit(material):
    def ambalaj(functia_noastra):
        def ambalaj_intern(*args):
            print(f'Ambalam produse din {functia_noastra.__name__} cu {material}')
            return f'{functia_noastra.__name__} cu {material}: {", ".join(x for x in  functia_noastra(*args))}'
            # return args
        return ambalaj_intern
    return ambalaj

@decorator_depozit('hartie')
def impachetare_carti(*args):
    return args

@decorator_depozit("folie alimentara")
def impachetare_fructe(*args):
    return args

print(impachetare_carti("Amintiri din copilarie", "Baltagul"))
# print(impachetare_fructe('mere', 'pere'))