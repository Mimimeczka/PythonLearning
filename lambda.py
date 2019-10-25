# '''LAMBDA'''
# dodaj = lambda a, b: a+b
# print(dodaj(3, 4))
#
# lista = [dodaj(x, y) for x, y in ([10, 20], [30, 40])]
# print(lista)
#
# print((lambda a, b: a*b)(10, 20))
#
# def obliczenie(n):
#     return lambda m: n+m
# y = obliczenie(30)
# print(y(4))
#
# lista = sorted(range(-5, 5), key = lambda k: k**2)
# print(lista)