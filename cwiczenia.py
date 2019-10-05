# wyraz = "kajak"
# print(wyraz == wyraz[::-1])



# imiona = ["Kinga", "Zofia", "Kamila", "Szymon", "Kuba", "Marian", "Waldek"]
# for y in imiona:
#     if y.startswith("K"):
#         imiona.remove(y)
# print imiona

# imiona.reverse()
# print (imiona)
#
# imie = "Jarek"
# print (imie.replace("J", "M")) # podmienie element
# print (imie)
# #rekJa
# print(imie [-3:] + imie [:2])

# powitanie = "Czesc {0:s}!"
# print(powitanie.format("Jarek"))
#
# ciag = "alodksncjska"
# waz = (len(ciag) / 2)
# print(ciag [: int(waz)])

# print(imie[1 : -1])
#
# print(imie[-2:] *3)
#
# napis1 = "Jarek"
# napis2 = "Justyna"
# #arekustyna
# print(napis1[1:] + napis2 [1:])
#
# x = "<<>>"
# y = "napis"
# #<<napis>>
# print(x[:2] + y + x[-2:])
#
#
#
# x2="aa"
# x1="Justyna"
# print(max(x1,x2) + min(x1, x2) + max(x1, x2))
# #aaJustynaaa
# # print(x1 + x2 + x1)
#
#
# liczby = range(0, 11)
# x = 5
# print(x in liczby)
#
# tab = [1, 2, 3]
# tablicaa_nowa = []
# tablicaa_nowa.append(tab[2])
# tablicaa_nowa.append(tab[2])
# tablicaa_nowa.append(tab[2])
# print(tablicaa_nowa)

# tab = [1, 2, 3, 4, 5, 6]
# tab2 = []
# tab2.append(tab[0])
# tab2.append(tab[-1])
# print(tab2)

# tab = [1, 2, 3, 4]
# tab2 = [1, 3, 5, 7]
# print(tab.count(2) != 0 or tab.count(4) != 0)
# print(tab2.count(2) != 0 or tab2.count(4) != 0)
# print(2 in tab or 4 in tab)
# print(2 in tab2 or 4 in tab2)


# tab = ["a", 2, 4]
# tab2 = [1, 2, 3, 1]
# print(tab[0] == tab[-1])
# print(int(tab2[0]) == int(tab2[-1]))

# tab = [1, 2, 3, 6]
# tab2 = [6, 1, 6]
# # print(tab[0] == 1 or tab[0] == 6 or tab[-1] == 1 or tab[-1] == 6)
#
#
#
#
# tekst = "Miala, baba koguta i wsadzila go do buta"
# nowy_tekst= ""
# slowa = tekst.split(" ")
# powtorzenia = 0
# for slowo in slowa:
#     nowy_tekst += slowo + " "
#     powtorzenia +=1
#     if powtorzenia >= 3:
#         print(nowy_tekst)
#         break



import random
# tablica = []
# # for x in range(10):
# #     tablica.append(random.randint(1, 10))
# # print(tablica, min(tablica), max(tablica))
# # print(sum(tablica))



# tablica = []
# x = 0
# while x < 10:
#     y = random.randint(1, 20)
#     if y % 2 != 0 and y not in tablica:
#         tablica.append(y)
#         x+=1
# tablica.sort()
# print(tablica)



# lista = []
# liczba = int(input("podaj liczbe: "))
# liczbax = int(input("podaj liczbe: "))
# lista.append(liczba + liczbax)
# lista.append(liczba - liczbax)
# lista.append(liczba * liczbax)
# if liczbax != 0:
#     lista.append(liczba / liczbax)
# print(lista)




# liczba = int(input("podaj liczbe:"))
# x = 1
# while x < liczba + 1:
#     print("o" * x)
#     x += 1




# id = {"nitka" : "igla", "waz" : "rzeczny", "dupa" : "wolowa"}
# login = input("LOGIN: ")
# haslo = input("HASLO: ")
# if login in id.keys() and haslo == id[login]:
#     print("zalogowany\\a")
# else:
#     print("wypierdalaj nie masz dostepu")



# '''ZMIENNE są zagospodarowaną częśiom pamięci w komputerze, która przechowuje pewne informacje jakiejś wartości
# Mogą przechowywać różne wartości: słowa, liczby
# Mają różne typy:
# STRING = czyli zmienna typu znaków = x
# INTEGER = czyli zmienna typu intiger = a, b
# FLOAT = czyli zmienna zmienno - przecinkowa = c
# Python jest dynamiczny czyli sie sam domyśli'''
# x = "Przechowywany tekst"
# a = 3
# b = 5
# c = 3.4
# wynik = a * b * c
# suma = a + b
# roznica = a - b
# iloraz = a / b
# potega = a ** b
# print(x)
# print("x")
# print(a)
# print(b)
# print(c)
# print(wynik)
# print(suma)
# print(roznica)
# print(iloraz)
# print(potega)



# '''STRING = STRI'''
# x = "Przechowuje tekst"
# y = x[0] + x[1] + x[2] + x[3] + x [4], " - to jest wyciety tekst"# podzmienna x
# '''W pytchonie zakres z leej strony jest zawsze zamknięty a z prawej otwarty
# Każda zmienna jest obiektem'''
# print(x[0:10])
# print(y)
# print(type(x)) # sprawdzanie typu zmiennej
# print(x[2]) # wypisywanie znaku na podanym miejscu
# '''dodawanie konkretnego znaku do obiektu'''
# a = "wazrzeczny"
# dodanie_spacji = a[0:3] + " " + a[3:]
# print(dodanie_spacji)




'''Komentarze są informacją dla nas, która nie jest brana pod uwagę tylko informuje nas
 o tym co robi dana cześć kodu, do czego służy dany fragment kodu lub za pomocą komentarza można
 wyłączać konkretne linijki kodu a podem można ją włączyc po jej wyłączeniu'''




# '''Arytmetyka'''
# liczba1 = 5
# liczba2 = 31
# liczba3 = 36
# suma = liczba1 + liczba2
# roznica = liczba1 - liczba2
# iloczyn = liczba1 * liczba2
# iloraz = liczba1 / liczba2
# potegowanie = liczba1 ** liczba2
# calkowita = liczba2 // liczba1 # dzielenie i wypisanie całości
# reszta = liczba2 % liczba1 # dzielenie i wypisanie tylko reszty
# print("Wynik dzielenia %d przez %d to %d calosci i %d reszty" %(liczba2, liczba1, calkowita, reszta))
#
# '''pierwiastkowanie'''
# pierwiastek = liczba3 ** 0.5 # pierwiastek z danej liczby
# import math
# pierwiastek2 = math.sqrt(liczba3)
# print(round(pierwiastek)) # wyświetla liczbe bez przecinka
# print(math.floor(pierwiastek)) # wyświetlanie liczby bez przecinka
# print(pierwiastek2)
#
# liczba3 = liczba3 + 4 # znak = nie porównuje tylko podstawia
# liczba3 += 4 # to samo co wyżej można zastosować każdy znak (-, +, *, **, /)
# print(liczba3)





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



# '''wyswietlanie liczb parzystych'''
# for x in range(0, 20, 2):
#     print(x)
# '''wszystkie liczby podzielne przez 5, oraz ich zsumowanie'''
# suma = 0
# iloczyn = 1
# for x in range(5, 100, 5):
#     suma += x
#     iloczyn *= x
# print("suma = ", suma, "iloczyn = ", iloczyn)




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

# '''obliczenie sumi 1 - 1000 wszystkich oraz tych podzielnych przez 3 a następnie obliczenie sumy liczb niepodzielnych przez 3'''
# suma = 0
# for x in range(1, 1000):
#     suma += x
# suma3 = 0
# for x in range(3, 1000, 3):
#     suma3 += x
# print("suma wszystkich liczb = ", suma)
# print("suma liczb podzielnych przez 3 = ", suma3)
# print("suma liczb niepodzielnych prez 3 = ", suma - suma3)
#
# podzielne = 0
# niepodzielne = 0
# for x in range(1, 1000):
#     if x % 3 == 0:
#         podzielne += x
#     else:
#         niepodzielne += x
# print("suma wszystkich liczb = ", podzielne + niepodzielne)
# print("suma liczb podzielnych przez 3 = ", podzielne)
# print("suma liczb niepodzielnych prez 3 = ", niepodzielne)
#
# by3 = 0
# all = 0
# for x in range(1, 1000):
#     if x % 3 == 0:
#         by3 += x
#     all += x
# print("suma wszystkich liczb = ", all)
# print("suma liczb podzielnych przez 3 = ", by3)
# print("suma liczb niepodzielnych prez 3 = ", all - by3)




# '''rzutowanie zmiennych'''
# liczba = 55.7
# print(round(liczba)) # zaokrągli liczbę  rzeczywistą i wyświetli całkowitą
# print(int(liczba)) # odetnie to co jest po przecinku i wyświetli liczbę całkowitą




# '''zagnieżdzanie pętli'''
# for x in range(0, 3):
#     print("wewnętrzna pętla for")
#     for y in range(0, 4):
#         print(x, y)

# '''WYPISUJE W PIONIE'''
# for x in range(0, 11):
#     for y in range(0, 11):
#         print("%d * %d = %d" % (x, y, x * y))
#
# '''WYPISUJE W POZIOMIE'''
# for x in range(0, 11):
#     for y in range(0, 11):
#         print("%d * %d = %d" % (x, y, x * y), end="\t")
#     print("\n")

# '''Napisz program, który wyswietli wszytskie mozliwe kombinacji czterocyfrowej kłódki gdzie pierwsza liczba jest parzysta
# druga nieparzysta trzecia podzielna przez 5 a czwarta podzielna przez 3'''
# np = 2353
# for x in range(0, 10, 2):
#     for y in range(1, 10, 2):
#         for z in range(0, 10, 5):
#             for t in range(0, 10, 3):
#                 print(x, y, z, t)

# '''napisz program przypominający możliwe kody do jego kłudki
# pamieta, że kłudka ma 5 cyfr, żadna nie jest większa niz 6 nie było w kodzie 0, pierwsza, trzecia i piąta cyfra to albo 0 albo 5,
# druga i czwarta były nieparzyste
# znależć w jaki sposób poprawić program z tabliczką mnożenia by odpowiedno się formatował'''
#
# for x in range(0, 7, 5):
#     for z in range(1, 7, 2):
#         for y in range(0, 7, 5):
#             for c in range(1, 7, 2):
#                 for a in range(0, 7, 5):
#                     print(x, z, y, c, a)
#
# for x in range(11):
#     line = str(x)  # linijka tekstu dla tego wiersza
#     for y in range(11):
#         line += ("\t%3d" %(x*y))
#     print(line)




# '''INSTRUKCJA WARUNKOWA = służy by pewna częśc kodu została wykonana wtedy i tylko wtedy'''
# i = 3
# if i > 0:
#     print(i)

# for i in range(1, 100):
#     if i % 17 == 0:
#         if i % 2 == 0:
#             print("liczba %d jest podzielna zarówno przez 17 jak i jest parzysta" %(i))
#         print("liczba  %d jest podzielna przez 17" %(i))

# for x in range(0, 11):
#     for y in range(0, 11):
#         if x * y < 100:
#             print(" ", end="")
#         if x * y < 10:
#             print(" ", end="")
#         print(" " + str(x * y), end="")
#     print("")

# for x in range(0, 11):
#     for y in range(0, 11):
#         print(" [:3]".format(y * y), end="")
#     print("")



# '''OPERATORY PORÓWNYWANIA: ==, >, < sprawdzają poprawność jakiegoś warunku
# == sprawdenie czy lewa stronna jest równa prawej
# = przypisanie lewej stronie prawą
# > sprawdzenie czy lewa strona jest większa od prawej
# < sprawdzenie czy lewa strona jest mniejsza od prawej
# >= sprawdzenie czy lewa strona jest większa od prawej bądź jest równa
# <= sprawdzenie czy lewa strona jest mniejsza od prawej bądź jest równa
# != sprawdzenie czy strony są różne
# '''
#
# x = input("liczba: ")
# if int(x) > 0:
#     print("liczba dodatnia")
# elif int(x) < 0:
#     print("liczba ujemna")
# else:
#     print("zero")

# '''LICZENIE DELTY'''
# import math
# import sys
# try:
#     a = int(input("a = "))
#     b = int(input("b = "))
#     c = int(input("c = "))
#     delta = b**2 - 4 * a * c
#     if delta > 0:
#         x1 = (-b - math.sqrt(delta)) / (2 * a)
#         x2 = (-b + math.sqrt(delta)) / (2 * a)
#         print("x1 = %d" % x1)
#         print("x2 = %d" % x2)
#     elif delta == 0:
#         x1 = -b / 2
#         print("x1 = %d" % x1)
#     else:
#         print("brak miejsc zerowych")
# except ValueError as e:
#     print("Nie można wpisywać liter, proszę podać cyfrę", e)
# except:
#     print("blad", sys.exc_info()[0])

# '''OPERATORY LOGICZNE
# and zanczy i jest operatorem koniunkcji sprawdza czy obie wartości są jednocześnie prawdziwe
# or znaczy lub jest operatorem alternatywnym, który sprawdza czy któraś z dwóch wartości jest prawdziwa
# not znaczy nie jest operatorem zaprzeczenia sprawdza czy zdanie loiczne jest fałszywe'''
# liczba = int(input("podaj liczbe w przedziale 10 - 20 lub 35: "))
# if (20 <= liczba > 10) or liczba == 35:
#     print("poprawnie")
# else:
#     print("niepoprwanie")

# '''ZMIENNE LOGICZNE - służą do przechowywania wyników porównań, które  zwracane są przez operatory logiczne
# bądź z operatorów porównywania
# Przy pomocy zmiennych logicznych możemy zapamiętać wynik ostatniego sprawdzenia i użyć go w późniejszym czasie'''
# print(3 > 5)
# print(6 > 5)
# '''False i True - przyjmują zmienne logiczne typu bool'''
# print(type(5 > 4))
# x = 5 > 6 # przechowywanie wartości
# y = 7 < 19 or 10 > 10
# print(x, y)
# liczba = int(input("podaj dowolną liczbę: "))
# czy_sie_dzieli_przez_2 = liczba % 2 == 0
# czy_sie_dzieli_przez_3 = liczba % 3 == 0
# czy_sie_dzieli_przez_5 = liczba % 5 == 0
# if czy_sie_dzieli_przez_2:
#     print("liczba podzielna przez 2")
# if czy_sie_dzieli_przez_3:
#     print("liczba podzielna przez 3")
# if czy_sie_dzieli_przez_5:
#     print("liczba podzielna przez 5")



# '''LICZBY PIERWSZE - naturalna liczba, która dzieli się przez 1 i samą siebie i jest wieksza bądź równa od 2'''
# liczba = int(input("podaj liczbe: "))
# for dzielnik in range(2, liczba):
#     if liczba % dzielnik == 0:
#         print("liczba %d dieli się przez %d i nie jest liczba pierwsza" % (liczba, dzielnik))
#         break
# else:
#     print("liczba %d jest liczbą pierwszą" % liczba)
#
# liczba = int(input("podaj liczbe: "))
# liczba_pierwsza = True
# for dzielnik in range(2, liczba):
#     if liczba % dzielnik == 0:
#         liczba_pierwsza = False
#         print("liczba %d dieli się przez %d i nie jest liczba pierwsza" % (liczba, dzielnik))
#         break
# if liczba_pierwsza:
#     print("liczba %d jest liczbą pierwszą" % liczba)

# for liczba in range(2, 1001):
#     liczba_pierwsza = True
#     for dzielnik in range(2, liczba):
#         if liczba % dzielnik == 0:
#             liczba_pierwsza = False
#             print("liczba %d dieli się przez %d i nie jest liczba pierwsza" % (liczba, dzielnik))
#             break
#     if liczba_pierwsza:
#         print("liczba %d jest liczbą pierwszą" % liczba)

# '''KŁÓDKA'''
# # ma 5 cyfr
# # największa możliwa do wprowadzenia cyfrą jest 8
# # nie ma ani 0 ani 6
# # suma cyfr wynosi 21
# # cyfry się nie powtarzają
# # iloczyn cyfr był >= 70
# # ostatnia cyfra jest nieparzysta
# ilosc = 0
# for a in range(1, 9):
#     for b in range(1, 9):
#         for c in range(1, 9):
#             for d in range(1, 9):
#                 for e in range(1, 9):
#                     if a != 6 and b != 6 and c != 6 and d != 6 and e != 6:
#                         if a + b + c + d + e == 21:
#                             if a != b and a != c and a != d and a != e and b != c and b != d and b != e and c != d and c != e and d != e:
#                                 if a * b * c * d * e >= 70:
#                                     if e % 2 != 0:
#                                         ilosc += 1
#                                         print(a, b, c, d, e)
# print("prob = %d" % ilosc)
#
# '''kłodka '''
# # 5 cyfr
# # licczba przedstawiająca kłódkę jest liczbą pierwszą
# # suma cyfr 30 - 40
# # nie było żadnego zera
# ilosc = 0
# for a in range(1, 9):
#     for b in range(1, 9):
#         for c in range(1, 9):
#             for d in range(1, 9):
#                 for e in range(1, 9):
#                     suma = a + b + c + d + e
#                     if suma <= 40 and suma >= 30:
#                         liczba = str(a) + str(b) + str(c) + str(d) + str(e)
#                         cyfra = int(liczba)
#                         liczba_pierwsza = True
#                         for dzielnik in range(2, cyfra):
#                             if cyfra % dzielnik == 0:
#                                 liczba_pierwsza = False
#                                 break
#                         if liczba_pierwsza:
#                             print("kod = %d" % cyfra)

# '''PĘTLA WHILE - w odróżńieniu do for nie jest wyonywana określoną ilość razy tylko dopóki dany warunek jest spełniony w nieskończoność'''
# liczba = int(input("podaj liczbe ujemna:"))
# while liczba > 0:
#     liczba = int(input("podaj liczbe ujemna:"))
# print("dodatnia wartość tej liczby = ", - liczba)





# '''LOSOWANIE LICZBY Z PRZEDZIAŁU I JEJ ODGADYWANIE'''
# import random
# y = random.randint(0, 100)
# x = int(input("Zgadnij liczbę z przediału 1 - 100 "))
# ilosc = 1
# while y != x:
#     if y > x:
#         ilosc += 1
#         print("podaj większą cyfrę")
#         x = int(input("Zgadnij liczbę z przediału 1 - 100 "))
#     else:
#         ilosc += 1
#         print("podaj mniejszą cyfrę")
#         x = int(input("Zgadnij liczbę z przediału 1 - 100 "))
#
# print("Odgadywana liczba to %d" % y)
# print("próbowałeś %d razy" % ilosc)


# '''Aby dokładnie kontrolować przepływ pętli while jak i for to można posłużyć się:
# continue - pomija jakąś część
# break - konczy pętlę'''
#
# '''LICZBY AMSTRONGA INACZEJ NARCYSTYCZNY
# które równają się sumie ich cyfr podniesionych do odpowiednich potęg
# np. 12 = 1 **2 + 2 **2 - nie jest
# np. 371 = 3 **3 + 7 **3 + 1 **3 - jest'''
#
# for liczba in range(0, 100000):
#     suma = 0
#     kopie = liczba
#     while kopie > 0:
#         cyfra = kopie % 10
#         suma += cyfra ** len(str(liczba))
#         kopie //= 10
#     if suma == liczba:
#         print("%d jest liczbą Amstronga" % liczba)
#
# napis = input("Podaj napis ")
# suma = 0
# while True:
#     if len(napis) == 0:
#         break
#     if len(napis) < 5:
#         napis = input("Podaj napis ")
#         continue
#     suma += len(napis)
#     napis = input("Podaj napis ")
# print("Suma znaków = ", suma)


# import random
# lista = []
# while len(lista) < 6:
#     numerek = random.randint(0, 50)
#     if numerek in lista:
#         numerek = random.randint(0, 50)
#         continue
#     lista.append(numerek)
# print(lista)



#
# lista = [["a", "b", "c"], ["g", "h", "o", "a"]]
# nowa = []
# for y in lista:
#     for z in y:
#         if z in nowa:
#             continue
#         nowa.append(z)
#         print(z, end = " ")
# print("\n")
# print(nowa)




# lista = [["a", "b", "c"], ["g", "h", "o", "a"]]
# nowa = {}
# for y in lista:
#     for z in y:
#         if z in nowa:
#             nowa[z] += 1
#         else:
#             nowa[z] = 0
#
# for c in nowa:
#     print(c, " = ", nowa[c])





# '''KOLEKCJE
# są to obiekty służące do przechowywania ewentualnie do innej operacji na innych obiektach
# np. aby posortować czy wydrukować
# LISTA - jedna z kolekcji'''
# lista = [] # pusta lista

# suma = 0
# zbior = []
# liczba = int(input("podaj liczbe: "))
# while liczba > 0:
#     suma += liczba
#     zbior.append(liczba)
#     liczba = int(input("podaj liczbe: "))
# print("srednia = ", suma / len(zbior))


# '''string i lista mają elementy wspólne'''
# lista = ["a", "b", "c"]
# napis = "abc"
# '''posiadają indeksy'''
# print(lista[1])
# print(napis[1])
# for element in lista:
#     print(element)
# for element in napis:
#     print(element)
# '''napis jest podobny do listy gdyż też jest kolekcjż znaków
# napis nie jest listą'''
# lista.append("d")
# napis = napis + "d"
# print(lista)
# print(napis)
# '''kiedy uzywamy append to mamy do czynienia z tą samą listą tylko z różnymi zawartościami w przypadku napisu
# był napis a potem stworzony całkiem inny nowy napis'''

# '''wypisywanie adresu pamięci'''
# lista = ["a", "b", "c"]
# napis = "abc"
# print(lista)
# print(id(lista))
# lista.append("d")
# print(lista)
# print(id(lista))
# print("--------")
# print(napis)
# print(id(napis))
# napis = napis + "d"
# print(napis)
# print(id(napis))
# '''tutaj widać, że po dodaniu obiektu do listy adres jest nadal taki sam, w przypadku napisu adres sie zmienia
# poprzedni napis został zniszczony'''


# '''MECHANIZM LOSOWANIA LICZB'''
# import random
# wylosowana = random.randint(1, 1000)
# print(wylosowana)
# '''losowanie 6 liczb'''
# import _random
# liczby = []
# razy = 0
# proba = 0
# while razy < 6:
#     liczba = random.randint(1, 100)
#     if liczba in liczby:
#         proba += 1
#         continue
#     else:
#         liczby.append(liczba)
#         razy += 1
#         proba += 1
# print(liczby)
# print(proba)
# '''funkcja random nie losuje przypadkowych liczb tylko je wylicza'''

# '''TUPLE / KRODKA - kolekcja
# podobna do list tylko różni się nawiasem
# można przechodzić po niej pętlą for
# różni się od listy tym, że nie są modyfikowalne czyli jeśli chcemy do niej dodatć coś nowego, gdyż po dodaniu stworzyła
# się nowa tupla posiadająca nowe zmienne, można to sprawdzić za pomocą id
# Jest nam ona potrzebna aby nikt jej nie modyfikował np inny programista czy program w trakcie działania
# działają czybciej ze względu na sposób przechowywania, który jest inny jak dla listy
# Jeśli nie chcemy później modyfikować kolekcji to lepiej jest zastosować tuple
# STR ma te same właściwości co tupla czyli jest niemodyfikowalny i po dodaniu coś do niego tworzy się coś nowego
# Czyli tupla jest bardziej podobna do STR niż do listy'''
# tupla = ("waż", 123, "rzeczny", 3.56)
# nowa = tupla + ("niebezpieczny",) # należy ustawić przecinek aby phyton wiedział, że chce dodać element a nie zmienna str

# '''Wszystkie dotychczas poznane kolekcje są ITEROWANE tzn. po nich można przejść od lewej do prawej, wszystkie
# mają indeksy po których można przejsc'''
# tupla = (1, 2, 3)
# lista = [4, 5, 6]
# string = "abc"
# '''WSPOLNE elementy
# -można je indeksować
# -wszystkie zaczynają się od 0'''
# lista2 = [9, 8, 7, tupla]
# print(lista2)
# '''w liście i w tupli można przechowywać dowolne obiekty a w pythonie wszystko jest obiektem'''
# tupla2 = (lista, 14, 146)
# print(tupla2)
# '''można kolekcje zagnieżdżać jedna w drugiej i to bardzo często'''
# '''indeks - [start:koniec:co ile ma przejsc]'''
# print(lista2[::-1]) # czytanie od tyłu
# print(lista2[::-2]) # co drugi element od tylu
# '''KONWERSJA czyli zamiana jednej kolekcji w drugą'''
# lista_z_string = list(string)
# lista_z_string[1] = "d" # zamiana w stringu b na d
# string = "".join(lista_z_string) # zrobienie nowego stringa z zamienioną literka i zrobienie z listy stringa
# print(string)

# '''KOLEKCJE DWUWYMIAROWE'''
# dwuwymiarowa_lista = [[1, 2, 3], [4, 5, 6]]
# print(dwuwymiarowa_lista[0][1]) # wyciaganie jednego elementu z listy w liscie
# '''wyciągniecie jednego elementu z listy w liscie'''
# for i in dwuwymiarowa_lista:
#     for j in i:
#         print(j, end=" ")
#     print()
# '''plansza do gry w szachy'''
# szachownica = (("K", "D", "A", "J", "U", "L", "O", "E"), ("P", "P", "P", "P", "P", "P", "P", "P"),
#                ("*", "*", "*", "*", "*", "*", "*", "*"), ("*", "*", "*", "*", "*", "*", "*", "*"),
#                ("*", "*", "*", "*", "*", "*", "*", "*"), ("*", "*", "*", "*", "*", "*", "*", "*"),
#                ("P", "P", "P", "P", "P", "P", "P", "P"), ("K", "D", "A", "J", "U", "L", "O", "E"))
# for i in szachownica:
#     for j in i:
#         print(j, end=" ")
#     print()

# '''ZBIÓR - jest kolekcja
# Nie jest iterowany
# kolejność nie koniecznie jest taka jaką my dodajemy
# Jest szybszy niż poprzednie kolekcje
# Nie dubluje takich samych wartości patrz 'gra w lotto' ta wersja jest o wiele szybsza niż poprzedniejsza '''
# zbior = {1, 2, 3}
# '''gra w lotto'''
# import random
# lotto = set() # tworzenie pustego zbioru
# while len(lotto) < 6:
#     lotto.add(random.randint(1, 50))
# print(lotto)
# lista = list(zbior) # stworzenie listy ze zbioru

# '''SŁOWNIK - kolekcja
# Różni się od pozostałych kolekcji tym, że posiada klucz i wartość i tym go indeksujemy
# Jeśli chcemy dostać się do jakiegoś elementu to wystarczy podać klucz'''
# slownik = {"Justyna Zaczyk": 734420071, "Andrzej Jakis": 582928645, "Jan Kowalski": 2744092638}
# sllownik = dict() # tworzenie słownika
# print(slownik["Justyna Zaczyk"])
# slownik["Andrzej Jakis"] = 684930275 # zmiana wartości



# '''1 sprawdzic jak otrzymac listę kluczy bądz listę wertości ze słowniki czyli posiadanie listy wartości
# 2 sprawdzić jakie są inne kolekcje dostepne w pythonie orderd string i orderd set, zbior posiadający powtarzające sie elementy
# 3 stworzenie podobnego słownika którego watrości zawsze są listy liczb nastepnie otrzymać liste wartości i wyswietlić
# wszystkie elementy z wew list
# oraz sumę wszystkich liczbowych wartości podobnie możesz zamienić listę na tuple'''
# slownik = {"ssak": "pies", "gad": "waz", "ryba": "pstrag", "ptak": "orzel"}
# lista_kluczy = slownik.keys()
# lista_wartosci = slownik.values()
# print(lista_kluczy)
#
# import collections
#
# wartosci = {"liczby parzyste": [0, 2, 4, 6, 8], "liczby nieparzyste": [1, 3, 5, 7, 9]}
# wartosci_wartosci = wartosci.values()
# suma = 0
# for x in wartosci_wartosci:
#     for y in x:
#         print(y)
#         suma += y
# print(suma)



# '''średnia arytmetyczna wybranej ilości liczb'''
# tablica = [int (x) for x in input("Podaj liczb do zsumowania oddzielając spacją: ").split("/")]
# suma = 0
# for x in tablica:
#     suma += x
# print("średnia tych liczb to ", suma / len(tablica))




# '''Srednia arytmetyczna za pomocą funkcji'''
# def SredniaArytmetyczna (liczby):
#     suma = 0
#     for x in liczby:
#         suma += x
#     return suma / len(liczby)
#
#
# do_zliczenia = [int(x) for x in input("Podaj liczb do zsumowania oddzielając spacją: ").split(" ")]
#
# print(SredniaArytmetyczna(do_zliczenia))




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



# '''GRA KÓŁKO I KRZYŻYK'''
# def wyswietl_plansze(mapa2D):
#     # ta funkcja jest odpowiedzialna za wyświetlenie planszy
#     print("  1 2 3")
#     numer_wiersza = 1
#     for wiersz in mapa2D:
#         print(numer_wiersza, end=" ")
#         for element in wiersz:
#             print(element, end=" ")
#         print()
#         numer_wiersza += 1
#
#
# def wygrana(mapa2D):
#     # ta funkcja jest odpowiedzalna za sprawdzenie wygranej
#     for x in range(0, 3):
#         if mapa2D[x][0] == mapa2D[x][1] and mapa2D[x][1] == mapa2D[x][2] and (mapa2D[x][2] == "o" or mapa2D[x][2] == "x"):
#             return True
#     for y in range(0, 3):
#         if mapa2D[0][y] == mapa2D[1][y] and mapa2D[1][y] == mapa2D[2][y] and (mapa2D[2][y] == "o" or mapa2D[2][y] == "x"):
#             return True
#     if mapa2D[0][0] == mapa2D[1][1] and mapa2D[1][1] == mapa2D[2][2] and (mapa2D[2][2] == "o" or mapa2D[2][2] == "x"):
#         return True
#     if mapa2D[2][0] == mapa2D[1][1] and mapa2D[1][1] == mapa2D[0][2] and (mapa2D[2][0] == "o" or mapa2D[2][0] == "x"):
#         return True
#     return False
#
#
# def remis(mapa2D):
#     # ta funkcja informuje o remisie
#     if not wygrana(mapa2D):
#         for wiersz in mapa2D:
#             for element in wiersz:
#                 if element == "*":
#                     return False
#         return True
#     else:
#         return False
#
# '''określenie kto zaczyna grac wcześniej'''
# graKrzyzyk = False
# pierwszy = input("Napisz 'x' jeśli pierwszy zaczyna a jesli nie to napisz 'o' ")
# if pierwszy == "x":
#     graKrzyzyk = True
#
# plansza = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
# # wyswietl_plansze(plansza)
#
# '''GRA - przebieg'''
# while (not remis(plansza)) and (not wygrana(plansza)):
#     wyswietl_plansze(plansza)
#     x, y = [int(x) for x in input("podaj wspolzedne pola w ktorym chcesz postawic znak: "). split()]
#     if plansza[x - 1][y - 1] == "*":
#         if graKrzyzyk:
#             plansza[x - 1][y - 1] = "x"
#             graKrzyzyk = False
#         else:
#             plansza[x - 1][y - 1] = "o"
#             graKrzyzyk = True
#
# '''informacja o wygranej'''
# wyswietl_plansze(plansza)
# if wygrana(plansza):
#     if graKrzyzyk:
#         print("wygrywa 'o' gratulujemy!!!")
#     else:
#         print("wygrywa 'x' gratulujemy!!!")
# else:
#     print("nastapil remis")

#
# '''zadanie zrobic sztuczna inteligencje'''
# '''zastosowc w ifach krotrzy zapis'''


#
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
# def silnia2(liczba):
#     # print("liczba = %d" % liczba)
#     if liczba == 1:
#         return 1
#     else:
#         # temp = liczba * (silnia2(liczba - 1))
#         # print("temp = ", temp)
#         return liczba * (silnia2(liczba - 1))
#
#
# y = int(input("Podaj liczbe z ktorej chcesz wyliczyc silnie: "))
# print("Silnia liczby %d wynosi %d" % (y ,silnia2(y)))



#
# '''SKRAWEK BIBLIOTEKI MATEMATYCZNEJ import match / from match import ...'''
# import math
# '''zaokraglanie'''
# print(round(3.6))
# print(math.floor(3.6)) # zaokrągla w dół
# print(math.ceil(3.4)) # zaokrągla w górę
# print(sum([1, 3, 18, 40, 27, 7])) # sumowanie listy, lepsze dla całkowitych
# print(math.fsum([1, 3, 18, 40, 27, 7])) # sumowanie listy, lepsze dla zmienno przecinkowych
# '''największy wspólny dzielnik'''
# print(math.gcd(19480, 17850380))
# '''pierwiastek'''
# print(math.sqrt(9))
# '''logarytmy'''
# print(math.log10(64))
# print(math.log(9, 3))
# print(math.sin(0))
# print(math.cos(0))
# '''stale matematyczna'''
# print(math.pi)
# print(math.sin(2 * math.pi))
# print(math.e)




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



'''wynik na system podajemy liczbe oraz system  11, 12...'''
'''jak zapisac krócej'''




# '''WSZYSTKO JEST OBIEKTEM
# każda kolekcja jest obiektem
# funkcja też jest obiektem'''
#
# def pomnoz(a, b):
#     return a * b
#
# def podziel(a, b):
#     return a / b
#
# def dodaj(a, b):
#     return a + b
#
# def odejmij(a, b):
#     return a - b
#
# def podzielCalkowicie(a, b):
#     return a // b
#
# def podzielReszte(a, b):
#     return a % b
#
# listaFunkcji = [pomnoz, podziel, dodaj, odejmij, podzielCalkowicie, podzielReszte]
# wyniki = ["mnozenia ", "dzielenia ", "dodawania ", "odejmowania ", "calosci dzielenia ", "reszty dzielenia "]
#
# a = float(input("Podaj liczbe "))
# b = float(input("Podaj liczbe "))
#
# for x in range(1, len(listaFunkcji)):
#     print("Wynik ", wyniki[x], "wynosi", listaFunkcji[x](a, b))
#
# '''Gdyby wszystko nie było obiektem to wykonanie byloby niemożliwe'''
#
#
# import dodatki
# liczby = []
# y = int(input("Podaj liczbe calkowita, jesli chcesz przestac podaj 0: "))
# while y != 0:
#     liczby.append(y)
#     y = int(input("Podaj liczbe calkowita, jesli chcesz przestac podaj 0: "))
#
# print("suma liczb wynosi ", dodatki.dodawanie(liczby))
# print("iloczyn liczb wynosi ", dodatki.mnozenie(liczby))




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



# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# suma = 0
# for x in lista:
#     suma += x
# lista.append(suma)
# print(lista)



# '''liczenie konkretnych liter w tekscie'''
# tekst = input("Podaj tekst: ")
# teksts = tekst.lower()
# lista = {}
# for x in teksts:
#     if x == " " and x == "," and x == ".":
#         continue
#     if x not in lista:
#         lista[x] = 1
#     else:
#         lista[x] += 1
# listas = sorted(lista.keys())
# for y in listas:
#     print(y, lista[y])
# '''inny sposob'''
# tekst = input("Podaj tekst ")
# teksts = set(tekst).difference(" ")# set oznacza robienie z liter zbioru natomiast difference pomija wybrany element
# slownik = dict((letter, tekst.count(letter)) for letter in teksts) # dict - tworzenie slownika
# slownikk = sorted(slownik.keys())
# for letter in slownikk:
#     print(letter, slownik[letter])



# '''klasa zbiór informacji
# funkcje w klasach są metodami zaś poza nimi są  funkcjami'''
# class Dog:
#     def giveVoice(self):
#         print("hauu hauu")
#
# misia = Dog
# latek = Dog
#
# misia.giveVoice()
# latek.giveVoice()


# '''Pola  w klasie sluża do tego by określić pewne cechy obiektu
# W klasie definiujemy z jakimi polami będziemy mieli do czynienia
# pola czyli zmienne
# A kazdy obiekt wypełnia je sobie sam'''
#
# '''mamy klase samochód i z niej bedziemy tworzyć pojedyncze obiekty czyli pojedyncze samochody
# '''
#
#
# class Car:
#     def __init__(self, model, brand, number): # metoda specjalna ta metoda wykonuje się zawsze kiedy obiekt jest tworzony, wykonuje sie wtedy kiedy tworzony jest obiekt
#         # po salfe piszemy te obiekty, które muszą być spełnione do stworzenia obiektu - KONSTRUKTOR
#         self.colour = ""
#         self.position = [0, 0]
#         self.model = model
#         self.brand = brand
#         self.number = number
#         self.speed = 0
#
#     def information(self):
#         print("Kolor mojego samochodu", self.colour)
#         print("Znajduje się moj samochod", self.position)
#         print("Model mojego samochodu", self.model)
#         print("Marka mojego samochodu", self.brand)
#         print("Numer rejestracyjny mojego samochodu", self.number)
#         print("Moj samochod porusza sie z predkoscia", self.speed)
#
#     def increaseSpeed(self, speed):
#         self.speed += speed
#
#
# myCar = Car("Fabia", "Skoda", "KNS 92876")
# youCar = Car("Fiesta", "Ford", "KN 98374")
# print(myCar)
# print(youCar)
# '''zostanie wyświetlona informacja gdzie są przechowywane dane informacje'''
#
# myCar.information()
# myCar.increaseSpeed(100)
# myCar.information()





# '''HERMETYZACJA - ukrywanie przed użytkownikiem klasy pól
# Pole to self.cos = cos
# zamiast z pola korzystamy z metod'''
#
# temp = float(input("Podaj temperature "))
# unit = input("Podaj jednostke c - Celcjusza / k - Kelvina / f - Fahrenhita ")
#
#
# '''Hermetyzacja polega na tym, że dostęp do jednej zmiennej opakowaliśmy w dwie metody
# Pobieranie temperatury jest zaszyte w klasie'''
#
#
# class Thermometer:
#     def __init__(self, temp):
#         self.celcjusz = temp
#
#     def setTemperature(self, temp, unit):
#         if unit == "c" or unit == "C":
#             self.celcjusz = temp
#         elif unit == "k" or unit == "K":
#             self.celcjusz = temp + 273.15
#         elif unit == "f" or unit == "F":
#             self.celcjusz = (5/9) * (temp - 32)
#         else:
#             print("Nieprawidlowa jednostka")
#
#     def getTemperature(self, unit = "c"):
#         if unit == "c" or unit == "C":
#             return self.celcjusz
#         elif unit == "k" or unit == "K":
#             return self.celcjusz - 273.15
#         elif unit == "f" or unit == "F":
#             return (self.celcjusz * (9/5)) + 32
#         else:
#             print("Nieprawidlowa jednostka")
#
# term = Thermometer(temp)
# term.setTemperature(temp, unit)
#
# while True:
#     choice = int(input("Wpisz 1 jesli chcesz chcesz otrzymac temperature w danej jednostce / Wpisz 2 jesli chcesz nadac inna temperature / Wpisz 3 jeśli chcesz zakonczyc "))
#     if choice == 3:
#         break
#     elif choice == 1:
#         unit = input("Podaj jednostke c - Celcjusza / k - Kelvina / f - Fahrenhita ")
#         print(term.getTemperature(unit))
#     elif choice == 2:
#         temp = float(input("Podaj temperature "))
#         unit = input("Podaj jednostke c - Celcjusza / k - Kelvina / f - Fahrenhita ")
#         print(term.setTemperature(temp, unit))
#     else:
#         print("Wybrano nieprawidłowo")
#         print("Sprobuj ponownie")
#         choice = int(input("Wpisz 1 jesli chcesz chcesz otrzymac temperature w danej jednostce / Wpisz 2 jesli chcesz nadac inna temperature / Wpisz 3 jeśli chcesz zakonczyc "))






# '''POROWNYWANIE OBIEKTOW
# sprawdzanie kiedy są identyczne
# Każdy obiekt ma inny adres pamięci wiec obiekty mimo iż są podobne to nie takie same
# gdyż posiadają inne miejsce'''
#
#
# class Cat:
#     def __init__(self, age, breed, name, hair):
#         self.age = age
#         self.breed = breed
#         self.name = name
#         self.hair = hair
#
#     def GetInformationAboutCat(self):
#         print("Kot %s ma %s lat, jest rasy %s, posiada %s kolor" %(self.name, self.age, self.breed, self.hair))
#
#     def setName(self, name):
#         self.name = name
#
# kot1 = Cat(3, "dachowiec", "Mruczek", "rudy")
# kot2 = Cat(5, "pers", "Kłaczek", "szary")
# kot3 = Cat(3, "dachowiec", "Mruczek", "rudy")
#
# print(kot1 ==kot2)
# print(kot3 ==kot2)
# print(kot1 ==kot3)
#
# kot1.GetInformationAboutCat()
# kot2.GetInformationAboutCat()
# kot3.GetInformationAboutCat()
#
# kot4 = kot1
# print(kot1 == kot4) # to jest ten sam kot
#
# '''zmiana coś w jednym obiekcie zmieniacoś w innym i obie nazwy oznaczają ten sam obiekt
# to jest ten sam obiekt'''
# kot4.setName("Piernik")
# kot4.GetInformationAboutCat()
# kot1.GetInformationAboutCat()






# '''KOLKO I KRZYZYK w sposob obiektowy'''
#
# class Board:
#     def __init__(self, player):
#         self.board = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
#         self.player = player
#         self.win = False
#
#     def checkInWin(self):
#         # ta funkcja jest odpowiedzalna za sprawdzenie wygranej
#         for x in range(0, 3):
#             if self.board[x][0] == self.board[x][1] and self.board[x][1] == self.board[x][2] and (self.board[x][2] == "o" or self.board[x][2] == "x"):
#                 self.win = True
#                 return True
#         for y in range(0, 3):
#             if self.board[0][y] == self.board[1][y] and self.board[1][y] == self.board[2][y] and (self.board[2][y] == "o" or self.board[2][y] == "x"):
#                 self.win = True
#                 return True
#         if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and (self.board[2][2] == "o" or self.board[2][2] == "x"):
#             self.win = True
#             return True
#         if self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2] and (self.board[2][0] == "o" or self.board[2][0] == "x"):
#             self.win = True
#             return True
#         return False
#
#     def checkIfDraw(self):
#         # ta funkcja informuje o remisie
#         if not self.checkInWin():
#             for wiersz in self.board:
#                 for element in wiersz:
#                     if element == "*":
#                         return False
#             return True
#         else:
#             return False
#
#     def printTheBoard(self):
#         # ta funkcja jest odpowiedzialna za wyświetlenie planszy
#         print("  1 2 3")
#         numer_wiersza = 1
#         for wiersz in self.board:
#             print(numer_wiersza, end=" ")
#             for element in wiersz:
#                 print(element, end=" ")
#             print()
#             numer_wiersza += 1
#
#     def checkIfFree(self, x, y):
#         return self.board[x - 1][y - 1] == "*"
#
#     def changeThePlayer(self):
#         if self.player == "o":
#             self.player = "x"
#         else:
#             self.player = "o"
#
#     def PutToBoard(self, x, y):
#         if self.checkIfFree(x, y):
#             self.board[x - 1][y - 1] = self.player
#             self.changeThePlayer()
#
#     def getPlayer(self):
#         return self.player
#
#     def returnBoard(self):
#         return self.board
#
#
#
# player = input("Napisz 'x' jeśli pierwszy zaczyna a jesli nie to napisz 'o' ")
#
# board = Board(player)
#
# while not board.checkInWin() and not board.checkIfDraw():
#     board.printTheBoard()
#     x, y = [int(x) for x in input("podaj wspolrzedne pola w ktorym chcesz postawic znak: ").split()]
#     board.PutToBoard(x, y)
#
# board.printTheBoard()
#
# '''informacja o wygranej'''
# if board.checkInWin():
#     if board.getPlayer() == "x":
#         print("wygrywa 'o' gratulujemy!!!")
#     else:
#         print("wygrywa 'x' gratulujemy!!!")
# else:
#     print("nastapil remis")




# '''DZIEDZICZENIE '''
#
# class Animal:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#
#     def printInformation(self):
#         print("nazywam się %s i mam %s lat" % (self.name, self.age))
#
#
#     def giveVoice(self):
#         raise NotImplementedError()
#
#
# class Marmal(Animal):
#     def __init__(self, age, name):
#         Animal.__init__(self, age, name)
#
#     def giveVoice(self):
#         print("Voice")
#
#     def go(self):
#         print("run")
#
#     def printInformation(self):
#         Animal.printInformation(self)
#         print("Jestem ssakiem")
#
#
# class Cat(Marmal):
#     def __init__(self, age, name, breed):
#         Marmal.__init__(self, age, name)
#         self.breed = breed
#
#     def giveVoice(self):
#         print("Mrauu")
#
#     def printInformation(self):
#         Marmal.printInformation(self)
#         print("Jestem kotem")
#
#
#
# class Dog(Marmal):
#     def __init__(self, age, name, boreed):
#         Marmal.__init__(self, age, name)
#         self.boreed = boreed
#
#     def giveVoice(self):
#         print("Hauu")
#
#     def printInformation(self):
#         Marmal.printInformation(self)
#         print("Jestem psem")
#
#
# # mruczek = Cat(5, "Mruczek", "Kot")
# #
# # mruczek.printInformation()
# # mruczek.go()
# # mruczek.giveVoice()
#
#
# import random
# zwierzeta = []
# imiona = ["Mruczek", "Rudzik", "Sniezek"]
# rasy = []
# for x in range(10):
#     losowanie = random.randint(0, 1)
#     random.shuffle(imiona)
#     if losowanie == 0:
#         zwierzeta.append(Cat(random.randint(0, 20), imiona[1], "Dachowiec"))
#     else:
#         zwierzeta.append(Dog(random.randint(0, 20), imiona[1], "Kundel"))
#
# zwierzeta[1].giveVoice()
#
# y = 1
# for x in zwierzeta:
#     print("Zwierze ", y)
#     x.printInformation()
#     y += 1


'''KLASA ABSTRAKCYJNA jest klasą z której nie chcemy tworzyć obiektów patrz klasa Animal'''

# class Animal:
#     def __init__(self):
#         raise Exception  # wyjatek
#
#     def printInformation(self):
#         pass
#
#
#     def giveVoice(self):
#         raise NotImplementedError()
#
#
# class Marmal(Animal):
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#
#     def giveVoice(self):
#         print("Voice")
#
#     def go(self):
#         print("run")
#
#     def printInformation(self):
#         print("nazywam się %s i mam %s lat" % (self.name, self.age))
#         print("Jestem ssakiem")
#
#
# class Cat(Marmal):
#     def __init__(self, age, name, breed):
#         Marmal.__init__(self, age, name)
#         self.breed = breed
#
#     def giveVoice(self):
#         print("Mrauu")
#
#     def printInformation(self):
#         Marmal.printInformation(self)
#         print("Jestem kotem")
#
#
#
# class Dog(Marmal):
#     def __init__(self, age, name, boreed):
#         Marmal.__init__(self, age, name)
#         self.boreed = boreed
#
#     def giveVoice(self):
#         print("Hauu")
#
#     def printInformation(self):
#         Marmal.printInformation(self)
#         print("Jestem psem")

'''inna metoda tworzenie klasy abstrakcyjnej'''

# from abc import ABC, abstractclassmethod
#
# class Animal(ABC):
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#
#     def printInformation(self):
#         print("nazywam się %s i mam %s lat" % (self.name, self.age))
#
#     @ abstractclassmethod # pokazanie, że dana klasa jest wirtualna
#     def giveVoice(self):
#         raise NotImplementedError()
#
#
# class Marmal(Animal):
#     def __init__(self, age, name):
#         Animal.__init__(self, age, name)
#
#     def giveVoice(self):
#         print("Voice")
#
#     def go(self):
#         print("run")
#
#     def printInformation(self):
#         Animal.printInformation(self)
#         print("Jestem ssakiem")
#
#
# class Cat(Marmal):
#     def __init__(self, age, name, breed):
#         Marmal.__init__(self, age, name)
#         self.breed = breed
#
#     def giveVoice(self):
#         print("Mrauu")
#
#     def printInformation(self):
#         Marmal.printInformation(self)
#         print("Jestem kotem")
#
#
#
# class Dog(Marmal):
#     def __init__(self, age, name, boreed):
#         Marmal.__init__(self, age, name)
#         self.boreed = boreed
#
#     def giveVoice(self):
#         print("Hauu")
#
#     def printInformation(self):
#         Marmal.printInformation(self)
#         print("Jestem psem")





# class Tetragon:
#     def __init__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
#     def perimeter(self):
#         return self.a + self.b + self.c + self.d
#
#     def area(self):
#         pass
#
# class Ractangle(Tetragon):
#     def __init__(self, a, b):
#         Tetragon.__init__(self, a, b, a, b)
#
#     def area(self):
#         return self.a * self.b
#
# class Square(Ractangle):
#     def __init__(self, a):
#         Ractangle.__init__(self, a, a)
#
#
# kwadrat = Square(4)
# prostokat = Ractangle(3, 5)
# figury = [kwadrat, prostokat]
#
# for figura in figury:
#     print("Pole figury wynosi ", figura.area())
#     print("Obwod figury wynosi ", figura.perimeter())

#



'''ZADANIE stworzenie klass z dziedziczeniem np. pojazdy '''





'''DZIEDZICZENIE WIELOKROTNE czyli dana klasa może odziedziczyć ceche z kilku klas'''


# class DuckBehaviour: # klasa calkowicie abstrakcyjna / opisuje zachowania kaczki
#     def Fly(self):
#         print("Latanie")
#
#     def Voice(self):
#         print("Kwa kwa")
#
#     def Go(self):
#         print("go go")
#
#
# class Duck(DuckBehaviour):
#     def __init__(self, name, age: int):
#         self.name = name
#         self.age = age
#
#
# class Toy:
#     def __init__(self, color, material):
#         self.color = color
#         self.material = material
#
#
# class ToyDuck(Toy, DuckBehaviour):
#     pass
#
#
# class Robot:
#     def __init__(self, typ):
#         self.typ = typ
#
#     def Voice(self):
#         print("I'm a robot")
#
#
# kaczka = ToyDuck("zolty", "guma")
# kaczka.Voice()
#
#
# '''POLOMORFIZM - wbudowany w język
# Mechanizm pozwalający na operowanie w różnych grupach w ten sam sposób np. przykład kaczki
# Można osiągnąć przy pomocy dziedziczenia lub też nie przykład Robot'''
#
# kaczuszka = Duck("Monika", 3)
# zabaweczka = ToyDuck("zolty", "guma")
# kaczatko = Duck("Sara", 9)
# zabawka = ToyDuck("pomaranczowy", "plastik")
# robocik = Robot("zabawka")
# lista = [kaczuszka, zabaweczka, kaczatko, zabawka, robocik]
# lista[1].Voice()
#
# '''przyklad 1'''
# print("przyklad 1")
# for element in lista:
#     if hasattr(element, "Fly"): # sprawdza czydany objekt posiada daną cechę
#         element.Fly()
#     else:
#         print("Objekt %s nie posiada metody Fly" % element)
#
# '''przykład 2'''
# print("przyklad 2")
# for element in lista:
#     try:
#         element.Go()
#     except:
#         print("Objekt %s nie posiada metody Fly" % element)
#
# '''W przypadku jeśli chcemy wywołać kilka metod na raz do tego zdecydowanie lepszy
# jest przykład 2'''
# '''przyklad 1'''
# print("przyklad 1")
# for element in lista:
#     if hasattr(element, "Fly") and hasattr(element, "Go") and hasattr(element, "Voice"):
#         element.Fly()
#     else:
#         print("Objekt %s nie posiada metody Fly" % element)
# '''przykład 2'''
# print("przyklad 2")
# for element in lista:
#     try:
#         element.Fly()
#         element.Go()
#         element.Voice()
#     except:
#         print("Objekt %s nie posiada metody do wywolania" % element)
#
# '''kolejny przykład polimorfizmu'''
# tablica = ["a", "b", "c"]
# krodka = "abd"
# liczba = 123
# def Read(napis):
#     return napis
# print(Read(tablica))
# print(Read(krodka))
# print(Read(liczba))


'''PROGRAMOWANIE OBIEKTOWE - PODSUMOWANIE
-styl spęłniające jakieś koncepcje: abstrakcja, hermetyzacja, dziedziczenie, polimorfizm
abstrakcja - budowanie programu dla naszego uzmysłowniena  uprzedmiotowienie, mamy do czynienia bardziej z obiektami 
niż z funkcjami, uogólnianie problemu, jest to uogólnianie pewnych rzeczy
 hermetyzacja - proces ukrywania pewnych danych, ukrywanie zmiennych by nie były dostępne poza klasą
 ukrywa implementacje np. self.__a = 5, 
 dziedziczenie - polegna na przejmowaniu cech klasy bazowej przez klasy pochodne
 polimorfizm - mechanizm pozwalanjący na operowanie na wielu różnych obiektach w ten sam sposób'''





'''DEKORATORY - dzieki nim możemy towrzyć i zaznaczać metody, które są klasowe bądź statyczny tzn jakaś metoda może działać bez instancji
czyli obiektu i działa na samej klasie, sama klasa też jest obiektem 
Obiekt zaczynamy pisać od "@" i nie potrzebujemy do tego obiektu czyli "self". Obiekt można utworzyć ale nie jest on konieczny.
Dzięki dekarotorowi możemy tworzyć metody niewymagające tworzenia obiektu. Statyczne metody istnieją w każdym języku. 
Oba dokoratory nie potrzebują obiektu. Metoda "c" ma dostęp do klasy i posiada dostęp informację do klasy która ją wywołuje, 
a "s" nie ma dostępu. Dzięki cls mamy dostęp do klasy.'''

# class Numbers:
#     SumNumberss = 0
#
#     def __init__(self, numbers=[]):
#         self.numbers = numbers
#
#     def SumNumbers(self):
#         sumary = 0
#         for x in  self.numbers:
#             sumary += x
#         return sumary
#
#     def ProductNumbers(self):
#         product = 1
#         for x in self.numbers:
#             product *= x
#         return product
#
#     def AddNumber(self, number):
#         self.numbers.append(number)
#         Numbers.SumLista(number)
#
#     @classmethod
#     def SumLista(cls, number):
#         cls.SumNumberss += number
#
#     @staticmethod # metoda statyczna
#     def odejmowanie(a, b):
#         print("Jestem statyczna metoda")
#         return a - b
#
#     @classmethod # metoda klasowa
#     def PrintInformationAboutMe(cls):
#         print("Jestem klasowa metoda")
#         print("Wywołaną na rzecz klasy", cls.__name__)

#
#
# liczby = Numbers()
# liczby.AddNumber(5)
# liczby.AddNumber(6)
# print(liczby.SumNumbers())
# print(liczby.ProductNumbers())
# print(liczby.odejmowanie(4, 2))
# print(liczby.PrintInformationAboutMe())


# lista1 = Numbers([])
# lista1.AddNumber(3)
# lista1.AddNumber(5)
# print(lista1.SumNumbers())
# lista2 = Numbers([])
# lista2.AddNumber(30)
# lista2.AddNumber(50)
# print(lista2.SumNumbers())
# print(Numbers.SumNumberss)


'''Klasa oprócz metod powinna miec swoje pola (HowManyCar)(możemy się do nich odwoływać przy pomocy klas metod)'''
# class Car:
#     HowManyCar = 0
#
#     def __init__(self, brand):
#         self.brand = brand
#
#     @classmethod
#     def AddCar(cls):
#         cls.HowManyCar += 1
#
# samochod = Car("skoda")
# print(samochod.HowManyCar)
# print(Car.HowManyCar)
# samochod.AddCar()
# print(samochod.HowManyCar)
# print(Car.HowManyCar)

# '''INACZEJ'''
# class Car:
#     SumCar = 0
#     @classmethod
#     def __init__(cls, self, brand):
#         self.brand = brand
#         cls.SumCar += 1
#
# samochod = Car(Car, "fiat")
# print(samochod.SumCar)


import time
time.sleep(10)
print("waz")
