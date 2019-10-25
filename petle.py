# najmniejsza = None
# najwieksza = None
# line = input("Podaj liczbe jeśli chcesz skończyć wciścnij 'k' ")
# while len(line):
#     line = int(line)
#     if najmniejsza is None or line < najmniejsza:
#         najmniejsza = line
#     if najwieksza is None or line > najwieksza:
#         najwieksza = line
#     line = input("Podaj liczbe jeśli chcesz skończyć wciścnij 'k' ")
#
# print(f"najwieksza liczba to {najwieksza}")
# print(f"najmniejsza liczba to {najmniejsza}")



# najmniejsza = None
# najwieksza = None
# line = input("Podaj liczbe jeśli chcesz skończyć wciścnij 'k' ")
# while True:
#     if line == "k":
#         break
#     line = int(line)
#     if najmniejsza is None or line < najmniejsza:
#         najmniejsza = line
#     if najwieksza is None or line > najwieksza:
#         najwieksza = line
#     line = input("Podaj liczbe jeśli chcesz skończyć wciścnij 'k' ")
#
# print(f"najwieksza liczba to {najwieksza}")
# print(f"najmniejsza liczba to {najmniejsza}")






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






# import random
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





# '''ELSE W PĘTLI'''
# import random
# my_number = random.randint(0, 1000)
# guess = 2
# ile_razy = 0
# odgadywanie = int(input("Podaj liczbe z przedziału 1 - 1000 "))
# while 0 <= odgadywanie <= 1000:
#     if my_number > odgadywanie:
#         print("PODAJ WIEKSZA LICZBE")
#         ile_razy += 1
#         odgadywanie = int(input("Podaj liczbe z przedziału 1 - 1000 "))
#     elif my_number < odgadywanie:
#         print("PODAJ MNIEJSZA LICZBE")
#         ile_razy += 1
#         odgadywanie = int(input("Podaj liczbe z przedziału 1 - 1000 "))
#     else:
#         print("GRATULACJE, probowales: ", ile_razy + 1)
#         print("ODGADYWANA LICZBA TO", my_number)
#         break
#
# else:
#     print("wybrełeś liczbe z poza przedziału")
#     print("ODGADYWANA LICZBA TO", my_number)
#     print("KONIEC GRY")



