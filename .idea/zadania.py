'''sprawdzenie czy podana lista jest posortowana rosnąco'''
# lista = [1, 2, 3, 6, 8, 4, 5, 8]
# # lista = [1, 2, 3, 6, 8, 9, 12, 20]
#
# def lista_rosnaca(lista):
#     for x in range(len(lista) - 1):
#         if int(lista[x]) > int(lista[x +1]):
#             return False
#     return True
#
# print(lista_rosnaca(lista))


'''liczba doskonała'''
# def liczba_doskonała(liczba):
#     suma = 0
#     for i in range(1, int(liczba / 2) + 1):
#         if liczba % i == 0:
#             suma += i
#     if suma == liczba:
#         return ("Liczba %d jest liczbą doskonałą" % liczba)
#     else:
#         return ("Liczba %d nie jest liczbą doskonałą" % liczba)
#
#
# zapytanie = int(input("Podaj liczbę do sprawdzenia: "))
#
# print(liczba_doskonała(zapytanie))

'''liczby doskonałe'''
# def liczby_doskonałe(liczba):
#     suma = 0
#     liczby_doskonale_lista = []
#     for x in range(1, liczba):
#         for i in range(1, int(x / 2) + 1):
#             if x % i == 0:
#                 suma += i
#
#         if suma == x:
#             liczby_doskonale_lista.append(x)
#         suma = 0
#
#     return liczby_doskonale_lista
#
#
# print(liczby_doskonałe(10000))

'''inwersja'''
# x = [2, 6, 9, 4, 6, 0, 5, 7, 2, 8, 1]
# def inwersja(lista):
#     ilosc_par = 0
#     for x in range(len(lista) ):
#         for z in range(x + 1, len(lista)):
#             if lista[x] > lista[z]:
#                 print(lista[x], "-", lista[z])
#                 ilosc_par += 1
#     return ilosc_par
#
# print(inwersja(x))

'''zadanie ze skarbem'''
# import random
# tablica = [["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
#            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
#            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
#            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
#            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]
#
# def wyswietlanie_planszy():
#     x = 0
#     print("      1    2    3    4    5    6    7    8    9    10")
#     while x < len(tablica):
#         print("%3d" % (x + 1), tablica[x])
#         x += 1
#
# wyswietlanie_planszy()
# a = random.randint(0, 9)
# b = random.randint(0, 9)
# tablica[a][b] = "X"
# wyswietlanie_planszy()
#
# while True:
#     y, x = [int(x) for x in input("Podaj współżędne oddzielone spacja: "). split(" ")]
#
#     if tablica[y - 1][x - 1] == "X":
#         print("Wygrana")
#         break
#     else:
#         if a > y - 1:
#             print("w dol")
#         if a < y - 1:
#             print("w gore")
#         if b > x - 1:
#             print("w prawo")
#         if b < x - 1:
#             print("w lewo")

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


'''wyrazenia nawiasowe'''
def wyrazenia_nawiasowe(tekst, nawiasA, nawiasB):
    liczenie = 0
    for x in tekst:
        if liczenie == -1:
            return False
        if x == nawiasA:
            liczenie += 1
        if x == nawiasB:
            liczenie -= 1
    if liczenie == 0:
        return True
    else:
        return False

print(wyrazenia_nawiasowe("())(()(())", "(", ")"))