# '''interakcja z użytkownikiem - pobieranie od użytkownika danych'''
# text = input("tekst: ")
# print(text)
# '''rozpoznanie, że tekst jest liczbą'''
# text2 = float(input("tekst"))
# print(text2 * 2)

# '''program obliczający średnią arytmetyczną z trzech podanych przez użytkownika liczb'''
# print("Liczenie średniej arytmetycznej")
# a = float(input("liczba a: "))
# b = float(input("liczba b: "))
# c = float(input("liczba c: "))
# print("Srednia arytmetyczna a + b + c = ", (a + b + c) / 3)


# # liczenie średniej arytmetycznej
# line = input("Podaj liczbę ")
# doSredniej = 0
# zbior = []
# while len(line):
#     zbior.append(line)
#     lineint = int(line)
#     doSredniej += lineint
#     line = input("Podaj liczbę ")
# print("Średnia arytmetyczna twoich liczb to %d" % (doSredniej / len(zbior)))


# '''napisz program rozwiązujący tzn obliczający miejsca zerowe
# trójmianu kwadratowego np. 3x**2+5x-20, gdzie użytkownik będzie wprowadzać czynnik 3, 5, 20
#  czyli współczynniki trójmianu kwadratowego i zakładam ,że delta jest zawsze większa od zera i oblicz x1 i x2 inaczej miejsca zerowe '''
# import math
# a = float(input("liczba a: "))
# b = float(input("liczba b: "))
# c = float(input("liczba c: "))
# delta = b**2 - 4 * a * c
# x1 = (-b - math.sqrt(delta)) / (2 * a)
# x2 = (-b + math.sqrt(delta)) / (2 * a)
# print("delta = ", delta)
# print("x1 = ", x1)
# print("x2 = ", x2)


# '''Pętle pozwalają na  wykonywanie kawałka jednego kodu wiele razy czyli wielkorotnie może zostać
# wykonana jedna instrukcja '''
# print("poczatek")
# for x in range(1,6): # w przedziale nie ma nigdy ostatniej liczby
#     print(x)
#     i = input("podaj liczbę: ")
# print("koniec")





# '''LICZENIE ŚREDNIEJ ARYTMETYCZNEJ'''
# import sys
# try:
#     rangemax = int(input("ile liczb zliczamy: "))
#     suma = 0
#     for x in range(0, rangemax):
#         y = int(input("liczba: "))
#         suma += y
#     print("średnia arytmetyczna wynosi: ", suma / rangemax)
# except ZeroDivisionError as e:
#     print("Nie można wyliczyć średniej arytmetycznej z zera", e)
# except ValueError as e:
#     print("nie wolno podawać liter należy podać liczbe", e)
# except:
#     print(sys.exc_info()[0])

''' napisz programy liczące śr harmoniczną geometryczną i kwadratową, poczytać do czego służą'''

# '''ŚREDNIA HARMONICZNA
# WZRÓ = n / (1/x1 + ... + 1/xn)
# n = ilość liczb liczonych'''
# import sys
# try:
#     rangemax = int(input("ile liczb zliczamy: "))
#     suma = 0
#     for x in range(0, rangemax):
#         y = int(input("liczba: "))
#         suma += 1/y
#     print("średnia harmoniczna wynosi: ", rangemax / suma)
# except ZeroDivisionError as e:
#     print("Nie można wyliczyć średniej arytmetycznej z zera", e)
# except ValueError as e:
#     print("nie wolno podawać liter należy podać liczbe", e)
# except:
#     print(sys.exc_info()[0])

# '''ŚREDNIA GEOMETRYCZNA
# WZRÓ = pierwiastek n z iloczynu liczb)
# n = ilość liczb liczonych'''
# import sys
# try:
#     rangemax = int(input("ile liczb zliczamy: "))
#     iloczyn = 1
#     for x in range(0, rangemax):
#         y = int(input("liczba: "))
#         iloczyn *= y
#     print("średnia geometrycz wynosi: ", iloczyn ** (1 / rangemax))
# except ZeroDivisionError as e:
#     print("Nie można wyliczyć średniej arytmetycznej z zera", e)
# except ValueError as e:
#     print("nie wolno podawać liter należy podać liczbe", e)
# except:
#     print(sys.exc_info()[0])

# '''ŚREDNIA KWADRATOWA
# WZRÓ = pierwiastek suma kwadratów liczb nad ich ilość)'''
# import sys
# import math
# try:
#     rangemax = int(input("ile liczb zliczamy: "))
#     suma = 0
#     for x in range(0, rangemax):
#         y = int(input("liczba: "))
#         suma += y ** 2
#     print("średnia geometrycz wynosi: ", math.sqrt(suma / rangemax))
# except ZeroDivisionError as e:
#     print("Nie można wyliczyć średniej arytmetycznej z zera", e)
# except ValueError as e:
#     print("nie wolno podawać liter należy podać liczbe", e)
# except:
#     print(sys.exc_info()[0])