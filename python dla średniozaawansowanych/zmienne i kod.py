'''zmienne, funkcja, id i operator is'''
# a = b = c = 10
# print(a, "id: ", id(a))
# print(b, "id: ", id(b))
# print(c, "id: ", id(c))
# print()
# a = 20
# print(a, "id: ", id(a))
# print(b, "id: ", id(b))
# print(c, "id: ", id(c))
# print()
# a = b = c = [1, 2, 3]
# a.append(4)
# print(a, "id: ", id(a))
# print(b, "id: ", id(b))
# print(c, "id: ", id(c))
# print()
# x = 10
# y = 10
# print(x, "id: ", id(x))
# print(y, "id: ", id(y))
# print()
# y = y + 1 - 1
# print(x, "id: ", id(x))
# print(y, "id: ", id(y))
# print()
# y = y + 1234567890 - 1234567890
# print(x, "id: ", id(x))
# print(y, "id: ", id(y))

'''typy zmiennych: mutable i immutable'''
# days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
# workdays = days.copy()
# workdays.remove("sat")
# workdays.remove("sun")
# print(days)
# print(workdays)

'''automatyczna konwersja do typu logicznego'''

# line = input("Wybierz opcje:\n1 - 'load data'\n2 - 'export data'\n3 - 'analyze & predict'\n")
# while len(line):
#     if line.isdigit():
#         if int(line) == 1:
#             print("1 - 'load data'")
#         elif int(line) == 2:
#             print("2 - 'export data'")
#         elif int(line) == 3:
#             print("3 - 'analyze & predict'")
#         else:
#             print("Niepoprawna opcja")
#     else:
#         print("Podana wartość nie jest liczbą")
#     line = input("Wybierz opcje:\n1 - 'load data'\n2 - 'export data'\n3 - 'analyze & predict'\n")
# print("Zakończono")


# options = ['load data', 'export data', 'analyze & predict']
# def DisplayOptions(x):
#     for x in range(len(options)):
#         print(x + 1, options[x])
#     choice = input("Select option above or press enter to exit: ")
#     return choice
#
# wybor = DisplayOptions(options)
# print(wybor)
#
# while True:
#     if wybor == "":
#         print("Nie wybrano żadnej opcji")
#         break
#
#     else:
#         try:
#             wybor = int(wybor)
#             if wybor == 1:
#                 print(f"1 - {options[0]}")
#
#             elif wybor == 2:
#                 print(f"2 - {options[1]}")
#
#             elif wybor == 3:
#                 print(f"3 - {options[2]}")
#
#             else:
#                 print("Nie ma takiej opcji")
#                 break
#         except:
#             print("Nieprawidłowa wartość")
#             break
#
#
#     wybor = DisplayOptions(options)
#     print(wybor)
#
#
# print("Zakończono")


'''operacja na plikach w wyrażeniach logicznych'''
# import os
# sciezka = "zadanie_na_plikach"
#
# if os.path.isfile(sciezka):
#     with open(sciezka) as file:
#         read = file.read()
#         read_list = read.split(" ")
#         read_len_list = len(read_list)
#         print("Liczba słów: ", read_len_list)
#
# else:
#     open(sciezka, "x").close()
#     print("stworzono plik")

''''''

# import os
# sciezka = "zadanie_na_plikach"
#
# # os.remove(sciezka)
#
# def OpenFiles(sciezka):
#     with open(sciezka) as file:
#         read = file.read()
#         read_list = read.split(" ")
#         read_len_list = len(read_list)
#         return f"Liczba słów: {read_len_list}"
#
#
# result = os.path.isfile(sciezka) or open(sciezka, "x").close()
#
# if result == True:
#     files = OpenFiles(sciezka)
#     print(files)
#
# else:
#     print("stworzono plik")


'''Skrócona składnia instrukcji if i polecenie pass'''

# price = 123
# bonus = 23
# bonus_granted = False
#
# if bonus_granted:
#     price -= bonus
#
# print(price)
#
# price = 123
# bonus = 23
# bonus_granted = False
#
# print(price - bonus) if bonus_granted else print("Brak bonusu")


''''''

# rating = 3
#
# if rating == 5:
#     print('very good')
# elif rating == 4:
#     print('good')
# else:
#     print('weak')
#
# print('very good') if rating == 5 else print('good') if rating == 4 else print('weak')


''''''

# import datetime
#
# day = datetime.datetime.today().weekday()
# print(day)
#
# print("Pomagam mamie") if day == 0 else print("Pranie") if day == 1 or day == 2 else print("Dyzor") if day ==3 else print("Dwa zebrania") if day == 4 else print("Lekcje") if day == 5 else print("Dla nas!!!")


'''Polecenie else w pętlach'''

# import os
# import sys
# import urllib.request
#
# # os.remove("cwiczenie strony internetowe/kursy.html")
# # os.remove("cwiczenie strony internetowe/mobilo.html")
#
# data_dir = "cwiczenie strony internetowe"
# pages = [
#     {'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'},
#     {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},
#     {'name': 'kursy', 'url': 'http://www.kursyonline24.eu/'}
# ]
#
# for x in pages:
#     try:
#         path = data_dir + "/" + x["name"] + ".html"
#         urllib.request.urlretrieve(x["url"], path)
#     except urllib.error.URLError:
#         print("Nie ma takiej strony")
#         break
#     except:
#         print("Błąd: ", sys.exc_info()[0])
#         break
# else:
#     print("Wszystko poszło OK")


'''range, list, slice'''
# colors = ["red", "orange", "green", "violet", "blue", "yellow"]
#
# def color(list_colors, how_many_color):
#     color = list(list_colors.copy())
#     return color[: how_many_color]
#
# wybor = color(colors, 5)
# print(wybor)

''''''

# colors = ["brown", "red", "orange", "green", "violet", "blue", "yellow"]
#
# def color(list_colors, how_many_color):
#     color = list(list_colors.copy())
#     possibilities = 0
#     for p in range(0, len(color) - how_many_color + 1):
#         print(color[p: p + how_many_color])
#         possibilities += 1
#     return possibilities
#
# wybor = color(colors, 3)
# print(wybor)

# napis = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."
# print(napis[napis.find("(") + 1: napis.find(")")])

'''enumerate i zip'''
# projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
# dates = ['2016-06-23', '2016-08-29', '1994-01-01']
# leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
#
# for n, (p, d, l) in enumerate(zip(projects, dates, leaders)):
#     print(f"{n} - The leader of {p} started {d} is {l}")

'''iteracja po słowniku'''

# banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
# quantity_banknotes = [0] * len(banknotes_coins)
# dict_denominations = dict(zip(banknotes_coins, quantity_banknotes))
#
# dict_denominations[100] += 1
# dict_denominations[20] += 1
# dict_denominations[5] += 1
# dict_denominations[0.5] += 1
# dict_denominations[50] += 1
# dict_denominations[20] += 2
# dict_denominations[5] += 1
# dict_denominations[2] += 2
# dict_denominations[100] += 1
# dict_denominations[50] += 1
# dict_denominations[2] += 1
#
# for x in dict_denominations:
#     info = "Denominate: {0:8.2f} - amount {1:6d}"
#     print(info.format(float(x), int(dict_denominations[x])))


'''zadniezdzanie petli'''
# '''lista'''
# zagniezdzenie = [(a, b) for a in list(range(6)) if a % 2 != 0 for b in list(range(6)) if b % 2 == 0]
# print(zagniezdzenie)
# '''słownik'''
# zagniezdzenie = {a: b for a in list(range(6)) if a % 2 != 0 for b in list(range(6)) if b % 2 == 0}
# print(zagniezdzenie)
#
# ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
#          'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
# '''wszystkie mozliwe polaczenia'''
# polaczeniaA = [(p, k) for p in ports for k in ports]
# print(polaczeniaA)
# print("Ilość połączeń: ", len(polaczeniaA))
# '''gdzie p jest rozne od k'''
# polaczeniaB = [(p, k) for p in ports for k in ports if p != k]
# print(polaczeniaB)
# print("Ilość połączeń: ", len(polaczeniaB))
# '''pomijając duble'''
# polaczeniaC = [(p, k) for p in ports for k in ports if p < k]
# print(polaczeniaC)
# print("Ilość połączeń: ", len(polaczeniaC))
#
# polaczeniaD = []
# for x in ports:
#     for y in ports:
#         if x != y and (y, x) not in polaczeniaD:
#             polaczeniaD.append((x, y))
# print(polaczeniaD)
# print("Ilość połączeń: ", len(polaczeniaD))

'''generatory'''
# ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
#          'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
# '''wszystkie mozliwe polaczenia'''
# polaczeniaA = ((p, k) for p in ports for k in ports)
# for p in polaczeniaA:
#     print(p)
# '''gdzie p jest rozne od k'''
# polaczeniaB = ((p, k) for p in ports for k in ports if p != k)
# for p in polaczeniaB:
#     print(p)
# '''pomijając duble'''
# polaczeniaC = ((p, k) for p in ports for k in ports if p < k)
# for p in polaczeniaC:
#     print(p)


'''funkcja eval'''
# import math
# argument_list = []
# for x in range(0, 101):
#     argument_list.append(str(x/10))
#
# formula = input("Podaj wzór: ")
#
# for a in argument_list:
#     polecenie = ""
#     for z in formula:
#         if z == "x":
#             z = a
#         polecenie += z
#     wynik = eval(polecenie)
#     print(polecenie, "=", wynik)


'''funkcja exec'''
# import os
# files_to_process = [
#     r"cwiczenie strony internetowe/przykładA.py",
#     r"cwiczenie strony internetowe/przykładB.py"
#     ]
# for x in files_to_process:
#     print(os.path.basename(x))
#     print(x)
#     with open(x) as path:
#         read = path.read()
#         source = exec(read)

'''funkcja compile'''
import math
import time

print("Przykłąd pierwszy")
formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []
for i in range(10):
    argument_list.append(i/10)

results_list = []

stast = time.time()
for formula in formulas_list:
    print(formula)
    for argument in argument_list:
        new_formula = ""
        for sign in formula:
            if sign == "x":
                sign = str(argument)
            new_formula += sign
        operation = eval(new_formula)
        # print(operation)
        results_list.append(operation)
print("Maksymalna wartość z listy: ", max(results_list))
print("Minimalna wartość z listy: ", min(results_list))
stop = time.time()
print("Czas programu: ", stop - stast)

print("Przykłąd drugi")

stast2 = time.time()
for formula in formulas_list:
    print(formula)
    for argument in argument_list:
        new_formula = ""
        for sign in formula:
            if sign == "x":
                sign = str(argument)
            new_formula += sign
        operation = compile(new_formula, 'zmienne i kod.py', 'eval')
        results_list.append(eval(operation))
        # print(str(operation))

print("Maksymalna wartość z listy: ", max(results_list))
print("Minimalna wartość z listy: ", min(results_list))
stop2 = time.time()
print("Czas programu: ", stop2 - stast2)




