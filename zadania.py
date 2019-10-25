'''posortowana lista'''
# x = [1, 2, 3, 4, 5, 6, 7]
# # x = [2, 5, 8, 4, 3, 5, 6, 3, 3]
# def sprawdzanie_listy(lista):
#     for y in range(len(lista) - 1):
#         if lista[y] > lista[y + 1]:
#             return False
#     return True
#
# print(sprawdzanie_listy(x))

'''liczba doskonala'''
# def liczba_doskonala(liczba):
#     suma = 0
#     for x in range(1, int(liczba / 2) + 1):
#         if liczba % x == 0:
#             suma += x
#
#     if suma == liczba:
#         return True
#     else:
#         return False
#
# print(liczba_doskonala(60))

'''liczby doskonałe'''
# def liczby_doskonale(liczba):
#     suma = 0
#     znaleziono = 0
#     for x in range(1, liczba + 1):
#         for y in range(1, int(x / 2) +1):
#             if x % y == 0:
#                 suma += y
#
#         if suma == x:
#             print(f"Liczba {x} jest doskonałą")
#             znaleziono += 1
#         suma = 0
#
#     return znaleziono
#
# print("Znaleziono: " + str(liczby_doskonale(9999)))

'''inwersja'''
# def inwersja(lista):
#     para = 0
#     for x in range(len(lista)):
#         for y in range(x + 1, len(lista)):
#             if lista[x] > lista[y]:
#                 print(lista[x], "-", lista[y])
#                 para += 1
#     return para
#
# x = [1, 2, 5, 7, 4, 6]
# print("Znaleziono", inwersja(x))

'''skarb'''
# plansza = [["*" for x in range(10)]for y in range(10)]
#
# import random
# a = random.randint(0, 9)
# b = random.randint(0, 9)
# # plansza[a][b] = "s"
#
# def wyswietl_plansze():
#     liczba = 1
#     print("      1    2    3    4    5    6    7    8    9    10")
#     for linia in plansza:
#         print("%3s" % liczba, linia)
#         liczba += 1
#
# wyswietl_plansze()
# while True:
#     x, y = [int(x) for x in input("podaj wspolzedne oddzielone spacja: ").split(" ")]
#     plansza[x - 1][y - 1] = "O"
#     wyswietl_plansze()
#     plansza[x - 1][y - 1] = "*"
#     if a == x - 1 and b == y - 1:
#         print("WYGRANA")
#         break
#     if a > x - 1:
#         print("w dol")
#     if a < x - 1:
#         print("w gore")
#     if b < y - 1:
#         print("w lewo")
#     if b > y - 1:
#         print("w prawo")

'''sklep'''
# produkty = {1: ["banan", 5.5, 50], 2: ["jabłko", 2.3, 50], 3: ["pomarancze", 7.45, 50], 4: ["brzoskwinie", 9.75, 50]}
# dostep = "2020"
#
#
# def wyswietlanie_produktwo():
#     tekst = "produkt {0:4d} nazwa {1:20s} cena {2:.2f} zapasy {3:.2f}"
#     for i in produkty:
#         print(tekst.format(i, produkty[i][0], produkty[i][1], produkty[i][2]))
#
# def nowy_produkt():
#     nazwa = input("Nazwa nowego produktu: ")
#     cena = pobierz_liczbe("Cena nowego produktu: ")
#     waga = pobierz_liczbe("Waga nowego produktu: ")
#     return [nazwa, cena, waga]
#
#
# def pobierz_liczbe(wiadomosc):
#     while True:
#         try:
#             return float(input(wiadomosc))
#         except ValueError:
#             print("nieprawidlowa wartosc")
#
# while True:
#     osoba = int(pobierz_liczbe("1 - kupujacy\n2 - sprzedający \n0 - zakoncz "))
#     if osoba == 1:
#         kwota_do_zaplaty = 0
#         while True:
#             wyswietlanie_produktwo()
#             x = int(pobierz_liczbe("Podaj numerek wybranego produktu:"))
#             y = pobierz_liczbe("Ilość wybranego produktu w kg. ")
#             kwota_do_zaplaty += y *  produkty[x][1]
#             produkty[x][2] -= y
#             z = int(pobierz_liczbe('''1 - kontynuowac zakupy \n0 - zakonczyc zakupy'''))
#             if z == 0:
#                 print("Do zapłaty {0:.2f}".format(kwota_do_zaplaty))
#                 break
#
#     elif osoba == 2:
#         haslo = input("Podaj hasło:")
#         if haslo == dostep:
#             while True:
#                 funkcja = int(pobierz_liczbe("1 - dodaj nowy produkt \n2 - usun produkt \n3 - edycja produktu \n0 - wyjscie"))
#                 if funkcja == 1:
#                     parametry_produktu = nowy_produkt()
#                     produkty[len(produkty) + 1] = [parametry_produktu[0], parametry_produktu[1], parametry_produktu[2]]
#                 elif funkcja == 2:
#                     wyswietlanie_produktwo()
#                     produkt_usuwany = int(pobierz_liczbe("Podaj numer usuwanego produktu"))
#                     produkty.pop(produkt_usuwany)
#                 elif funkcja == 3:
#                     wyswietlanie_produktwo()
#                     edytowanie = int(pobierz_liczbe("Wybierz numerek produktu, który chcesz zmodyfikowac"))
#                     parametry_produktu = nowy_produkt()
#                     produkty[edytowanie] = [parametry_produktu[0], parametry_produktu[1], parametry_produktu[2]]
#                 else:
#                     break
#         else:
#             print("Hasło nieprawidłowe")
#     else:
#         break
