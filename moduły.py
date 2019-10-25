# '''UŚPIENIE'''
# import time
# import random
# print("start")
# czas_wylosowany = random.randint(0, 10)
# print("czas wylosowany", czas_wylosowany)
# gotowanie = time.sleep(czas_wylosowany)
# print("stop")




'''time.time może nam posłużyć do sprawdzenia ile dana implementacja może trwać'''
# import time
# import math
# lista = []
# t1 = time.time()
# print("początek")
# for x in range(1, 10000000):
#     lista.append(x ** 2)
# t2 = time.time()
# print("Pierwsza implementacja trwala ", t2 - t1)
# for y in range(1, 10000000):
#     lista.append(math.pow(y, 2))
# t3 = time.time()
# print("Druga implementacja trwala ", t3 - t2)
# print("koniec")
#
# '''lub'''
#
# lista = []
# time.clock()
# print("początek")
# for x in range(1, 10000000):
#     lista.append(x ** 2)
# print("Pierwsza implementacja trwala ", time.clock())
# for y in range(1, 10000000):
#     lista.append(math.pow(y, 2))
# print("Druga implementacja trwala ", time.clock())
# print("koniec")







# '''time.sleap i podane w nawiasie sekundy służą np. do odliczania czyli
# na jaki czas program ma być wstrzymany'''
# import time
# for x in range(1, 31):
#     print(31 - x)
#     time.sleep(1)
#
# '''dzisiejszy czas i data'''
# import datetime
# dzisiajesza_data = datetime.datetime.today()
# print("dzien ", dzisiajesza_data.day, "miesiac ", dzisiajesza_data.month, "rok ", dzisiajesza_data.year)



# import time
# for odliczanie in range(0, 31):
#     print(30 - odliczanie)
#     time.sleep(1)


# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# suma = 0
# for x in lista:
#     suma += x
# lista.append(suma)
# print(lista)