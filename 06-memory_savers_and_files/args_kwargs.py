# def my_function(*param_1):
#     return param_1
#
#
# print(my_function("string", "string1", "string2"))

# def num_sum(*var): # daca avem mai multi parametrii *var este declarata ultima ex. (param_1, *var)
#     suma = 0
#     print(var)
#     for item in var:
#         suma += item
#     return suma
#
# print(num_sum(1, 2, 3, 4, 5))


# def diff_vars(*params):
#     diferenta = 0
#     for item in params:
#         diferenta -= item
#     return diferenta
#
# print(diff_vars(1, 2, 3, 4))


def catalog(*args, **kwargs):
    return args, kwargs.keys()


print(catalog(1, 2, nume="Popa", prenume="Ionut", varsta="12"))