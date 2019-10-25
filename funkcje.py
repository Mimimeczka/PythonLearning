# def zmiana_tekstu(zmiana, duze):
#     def bez_zmian(tekst, ile_razy):
#         return tekst * ile_razy
#     def duzymi (tekst: str, ile_razy = 1):
#         return tekst.upper() * ile_razy
#     def malymi(tekst, ile_razy):
#         return tekst.lower() * ile_razy
#
#     if zmiana:
#         return bez_zmian
#     else:
#         if duze:
#             return duzymi
#         else:
#             return malymi
#
# proba = zmiana_tekstu(False, True)
# print(proba("jaja", 5))




'''OBIEKTY GLOBALNE I NIELOKALNE'''
'''ZAGNIEŻDŻANIE FUNKCJI'''

# def funkcjaPierwsza (x):
#     print("Zostałą wywołana pierwsza funkcja")
#
#     def funkcjaZagniezdzona (y):
#         x = 7
#         print("Została wywołana druga funkcja")
#         print("Parametr pierwszej do potęgi drugiej %d" % y ** 2)
#         print("Ten x z funkcji zagnieżdżonej", x)
#
#     funkcjaZagniezdzona(x)
#     print( "Ten x z funkcji pierwszej", x)
#
#
# funkcjaPierwsza(2)
#
#
# x = 2
#
# def jakasFunkcja():
#     # global x
#     x = 7
#     print(x)
#
# jakasFunkcja()
# print(x)


# y = 3
# def jedynka():
#     # global y
#     y = 4
#     def dwojka():
#         nonlocal y
#         y = 5
#         # print(y)
#     dwojka()
#     # print(y)
#
# jedynka()
# print(y)





# '''ZAMIANA SYSTEMÓW POZYCYJNYCH'''
# '''SYSTEM DWÓJKOWY
# 5 = 101
# 1011010101 = 1*1 + 2*0 + 4*1 + 8*0 + 16*1 + 32*0 + 64*1 + 128*1 + 256*0 + 512 *1
# pass # zablokowanie funkcji'''
#
# def xDziesietnego(n):
#     reszta = []
#     while n > 0:
#         reszta.append(n % 2)
#         n //= 2
#     reszta.reverse()
#     wynik = 0
#     for element in reszta:
#         wynik += element
#         wynik *= 10
#     wynik //= 10
#     return wynik
#
# n = int(input("Podaj liczbe w systemie dziesietnym "))
# print("Liczba w systemie dwojkowym wynosi ", xDziesietnego(n))
#
#
#
# def xDziesietnego(n):
#     reszta = []
#     while n > 0:
#         reszta.append(n % 2)
#         n //= 2
#     reszta.reverse()
#     wynik = ""
#     for element in reszta:
#         nelement = str(element)
#         wynik += nelement
#     return wynik
#
# n = int(input("Podaj liczbe w systemie dziesietnym "))
# print("Liczba w systemie dwojkowym wynosi ", xDziesietnego(n))




# def xDwojkowego(n):
#     potega = 1
#     wynik = 0
#     while n > 0:
#         wynik += (n % 10) * potega
#         potega *= 2
#         n //= 10
#     return wynik
#
#
# n = int(input("Podaj liczbe w systemie dwojkowym "))
# print("Liczba w systemie dziesietnym wynosi ", xDwojkowego(n))




# '''wypakowywanie elementów'''
# def wypakowywanie(a, b, c):
#     return a + b + c
#
# x = [3, 6, 9]
# dodawanie = wypakowywanie(* x)
# print(dodawanie)






# '''FUNKCJA - to wydzielony kawałek powtarzającego się kodu, który ułatwia zmianę wspólnej części kodu
# nawias przechowuje pewne elementy'''
# def sowa():
#     print("Obliczanie wyniku")
#     print("Otrzymany wynik")
# x = int(input("podaj liczbe calkowita "))
# y = int(input("podaj liczbe calkowita "))
# sowa()
# print("dodawanie: ", x + y)
# sowa()
# print("mnozenie", x * y)
# sowa()
# print("odejmowanie", x - y)
# sowa()
# print("dzielenie", x / y)

# def dodawanie (a, b):
#     print("wynik = ", a + b)
# y = int(input("podaj liczbe "))
# x = int(input("podaj liczbe "))
# dodawanie(x, y)

# '''WARTOSC ZWRACANIA FUNKCJI - return za to odpowiada'''
# def dodawanie(a, b,c):
#     return a + b + c
# def mnozenie(a, b, c):
#     return a * b * c
# def delta(a, b, c):
#     return b **2 - 4 * a * c
# x, y, z = [float(x) for x in input("podaj 3 liczby oddzielone spacja ").split()]
# wynik_dodawania = dodawanie(x, y, z)
# wynik_mnozenia = mnozenie(x, y, z)
# wynik_delty = delta(x, y, z)
# print(wynik_dodawania)
# print(wynik_mnozenia)
# print(wynik_delty)

# '''wartosc domyslna argumentu funkcji'''
# def suma_liczb(a = 0, b = 0, c = 0, d = 0):
#     return a + b + c + d
# print(suma_liczb(4, 5))
#
# def suma(listaliczb):
#     wynik = 0
#     for x in lista:
#         wynik += x
#     return wynik
# lista = []
# y = float(input("Podaj liczby do sumowania, jesli chcesz przestac nacisnij 0 "))
# while y != 0:
#     lista.append(y)
#     y = float(input("Podaj liczby do sumowania, jesli chcesz przestac nacisnij 0 "))
# print("suma = ", suma(lista))
# print("srednia = ", suma(lista) / len(lista))






# '''FUNKCJE REKURENCYJNE to typ funkcji, która wywołuje samą siebie
# a ta wywołuje samą siebie w nieskonczoność do momentu spełnienia danego warunku
# Przykładem funkcji rekurencyjnej jest silnia to iloczyn do liczby podanej
# '''
#
# # '''FUNKCJA NAPISANA JAWNIE DO LICZENIA SILNI'''
# # def silnia(liczba):
# #     # wyliczenie silni podaenej liczby
# #     iloczyn = 1
# #     for x in range(2, liczba + 1):
# #         iloczyn *= x
# #     return iloczyn
# #
# #
# # y = int(input("Podaj liczbe z ktorej chcesz wyliczyc silnie: "))
# # print("Silnia liczby %d wynosi %d" % (y ,silnia(y)))
#
# '''FUNKCJA NAPISANA REKURENCYJNIE DO LICZENIA SILNI'''
def silnia2(liczba):
    '''ta funkcja oblicza silnie'''
    # print("liczba = %d" % liczba)
    if liczba == 1:
        return 1
    else:
        # temp = liczba * (silnia2(liczba - 1))
        # print("temp = ", temp)
        return liczba * (silnia2(liczba - 1))


y = int(input("Podaj liczbe z ktorej chcesz wyliczyc silnie: "))
print("Silnia liczby %d wynosi %d" % (y ,silnia2(y)))

