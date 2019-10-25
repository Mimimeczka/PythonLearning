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






# '''rzutowanie zmiennych'''
# liczba = 55.7
# print(round(liczba)) # zaokrągli liczbę  rzeczywistą i wyświetli całkowitą
# print(int(liczba)) # odetnie to co jest po przecinku i wyświetli liczbę całkowitą




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
# import dodatki
# liczby = []
# y = int(input("Podaj liczbe calkowita, jesli chcesz przestac podaj 0: "))
# while y != 0:
#     liczby.append(y)
#     y = int(input("Podaj liczbe calkowita, jesli chcesz przestac podaj 0: "))
#
# print("suma liczb wynosi ", dodatki.dodawanie(liczby))
# print("iloczyn liczb wynosi ", dodatki.mnozenie(liczby))
