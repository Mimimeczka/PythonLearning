# mrugnięcie_okiem = 20 * 60 * 16 * 365 * 50 # mrugniecie okiem w ciagu 50 lat
# print(mrugnięcie_okiem)
# #
# na_minute= 20 # liczba uderzen na minute
# na_godzine= na_minute * 60
# na_dobe= na_godzine * 16
# na_rok = na_dobe * 365
# wiek = 50 # ilosc lat
# print(na_rok * wiek)
#
# minuta = 20 #liczba uderzen na minute
# godzina = 60
# doba = 16
# rok = 365
# wiek = 50 # ilosc lat
# print(minuta * godzina * doba * rok * wiek)
#
# ''' ilosc murgniec okiem w przeciagu 50 lat'''
#
# print("TVP1", "TVP2", "TVP3", "YVN", "POLSAT", "BBC", "HBO", "MTV")
#
# print("TVP1", "TVP2", "TVP3", "YVN", "POLSAT", "BBC", "HBO", "MTV", sep=";") #odpowiada za rozdzielenie znakiem jakim chcemy
# "\n" - nowa linia,"\t" - tabulator, "\a" - wydobyc dzwiek

# program = "TVN"
# czas = 18.00
# print("Moj ulubiony program jest na %s o %.2f" % (program, czas))

#
# quote = "A good programmer is someone who always looks both ways before crossing a one-way street"
# print(quote.upper()) #napis zamienia na duże litery
# print(quote.lower()) # napis zamienia na male litery
# print(quote.endswith("street")) # czy napis konczy sie na...
# print(quote.islower()) # czy jest apisany malymi literami
# print(quote.isupper()) # czy jest zapisany duzymi literami
# print(quote.upper().isupper())
# print(quote.find("one")) # na ktorej pozycji znajde slo z
# print(quote.replace("one", "1")) # zamiana jedno na drugie
# print(quote.replace("one", "1").replace("both", "2"))
# print(quote.split(" ")) # rozdzielanie duzego napisu na kilka malych
# print(quote.isdigit()) # czy wyglada jak liczba
# print(quote.isdecimal()) # czy wyglada jak liczba z przecinkiem
# print(quote.isalpha()) # czy ma literki
# print(quote.isalnum()) # czy ma literki i cyferki
#
# cos = r"A text/nAtext"  #lirał r powoduje, że wszystkie znaki specjalne nie będą interpretowane w napisie

# imie = "Malgorzata "
# nazwisko_rodowe = "Nowak "
# nazwisko_meza = "Sowa"
#
# nowe_imie =imie + nazwisko_rodowe + nazwisko_rodowe # konkatenacja napisów
# print(nowe_imie)
#
# muzyka = "'Uniwersal Fanfare' Jerry Goldsmitch 'Happy Together' Garry Bonner 'I ' m a Man' Steven Win a od "
# print(muzyka)
#
# muzyka1 = "'Uniwersal Fanfare' Jerry Goldsmitch\n'Happy Together' Garry Bonner 'I ' m a Man' Steven Winwood "
# print(muzyka1)
#
# muzyka2 = r"'Uniwersal Fanfare' Jerry Goldsmitch\n'Happy Together' Garry Bonner 'I ' m a Man' Steven Winwood " #surowy tekst
# print(muzyka2)
#
# muzyka3 = "'Uniwersal Fanfare' Jerry Goldsmitch 'Happy Together' Garry Bonner 'I ' m a Man' Steven Winwood '\a'"
# print(muzyka3)
#
# print("(\\(\\")
# print("( -.-)")
# print("0_(\")(\")")
#
# article = '''
# Platformowa strzelanka, wydana przez studio Virgin Games na komputery ośmiobitowe, w której gracz wciela się w pana Gumby
# poszukującego brakujących szarych komórek. W grze pojawiają się postacie znane z serialu Latający Cyrk Monty Pythona, a
# także przez moment słynny Arkanoid.'''
# print(article.upper())
# print(article.lower().replace("monty", "flying"))
# print(article.split(" "))
#
# print("to print the \\ you need to put \\ twice in your text like this: \\\ ")
# print("The best hits of '80s!!!")
# print('The best hits of \'80s!!!')
#
# '''int(text) uznaje za liczbe calkowita, float(text) uznaje za liczbe z przecinkiem
#  natomiast str(2) uznaje jako napis type(text) sprawdzenie czy to int czy str / lfoat(inf) oraz -float(inf) - nieskonczonosci'''
#
# amountPLN = 234
# USD = 3.65
# EUR = 4.24
# print("cur\texchange\tamount")
# amount = amountPLN / USD
# amount1 = amountPLN / EUR
# print(amount, amount1)

# text = "%s ma %d lat"
# print(text %("Jaroslaw", 25))
# text2 = "%20s ma %20d lat" # zarezerwowanie miejsc na teks
# print(text2%("Jaroslaw", 25))
# text3 = "{0:s} ma {1:d} lat"
# print(text3.format("Jaroslaw", 25))
# text3 = "{1:s} ma {0:d} lat"
# print(text3.format(25, "Jaroslaw"))
#
# ValueAsText = "123.45"
# factor = 1.23
# print("value is %s factor is %.1f value*factor = %.4f" %(ValueAsText, factor, float(ValueAsText) * factor))
#
# article2 = '''Pierwsza seria „Latającego cyrku” miała pierwotnie dawać główne pole do popisu Cleese’owi,
# ten chciał jednak współpracować z innymi. Tak oto powstała zorganizowana grupa, dla której utworzono rutynowe
# zasady działania. Każdy dzień pisania rozpoczynał się o 9:00 rano i trwał do 17:00. Na początku typowego tygodnia
# pracy Cleese i Chapman pisali w odosobnieniu jako jedna spółka autorska, Jones i Palin jako druga, a Idle pisał sam.
# Po kilku dniach cała grupa spotykała się wraz z Gilliamem i krytykowała nawzajem swoje scenariusze oraz wymieniała
# poglądy. Podchodzili do pisania demokratycznie. Jeśli coś rozśmieszyło większość, zatwierdzano to jako część programu.
# W podobny sposób obsadzano role – nie było problemów z egocentryzmem, gdyż każdy z Pythonów czuł się bardziej autorem
# niż aktorem. Po dobraniu i uporządkowaniu kolejności skeczy do danego odcinka, Gilliam miał wolną rękę w łączeniu ich
# w całość za pomocą wymyślnych animacji, uzbrojony w kamerę, nożyczki i farbę.
#
# Zanim wymyślono nazwę „Latający cyrk Monty Pythona”, powstało kilka innych tytułów roboczych, m.in. Owl Stretching
# Time (Pora rozciągania sów), Bunn, Wacket, Buzzard, Stubble and Boot, Gwen Dibley's Flying Circus (Latający Cyrk Gwen Dibley).
#
# Zespół miał bardzo konkretny pomysł na serial i był bardzo zawiedziony, gdy Spike Milligan nagrał swój program
# komediowy Q5 w nieco podobnym duchu. Pythoni przyznawali się do inspiracji Milliganem, lecz styl „Latającego cyrku”
# jest zdecydowanie inny. Wyróżniają go szczególnie niepowtarzalne animacje Gilliama, ale także proces wzajemnej krytyki
# i selekcji materiału.'''
#
# print("word python appears %d times" % article2.lower().count("python"))
#
# helloMessage = "Hello %s"
# print(helloMessage % ("Justyna"))
# print(helloMessage % ("Jarek"))
#
# hellomessage = "Hello {0:s}"
# print(hellomessage.format ('Justyna'))
# print(hellomessage.format ('Jarek'))
#
# wiadomosc = "czesc %s i %s"
# print(wiadomosc % ("Justyna", "Jarek"))
# wiadomoscx = "czesc {0:s} i {1:s}"
# print(wiadomoscx.format("Justyna", "Jarek"))
#
# dane = "%s ma %d lat a %s ma %d lat "
# print(dane % ("Justyna", 23, "Jarek", 24))
#
# danex = "{0:s} ma {1:d} lat a {2:s} ma {3:d} lat"
# print(danex.format("Justyna", 23, "Jarek", 24))
#
# linia = "%20s %20s %20d$"
# print(linia % ("ice cream", "cost", 3))
# print(linia % ("trip to Venice", "cost", 119))
# print(linia % ("pizza hawai", "cost", 6))
#
# liniax = "{0:20s} {1:20s} {2:20d}$"
# print(liniax.format("ice cream", "cost", 3))
# print(liniax.format("trip to Venice", "cost", 119))
# print(liniax.format("pizza hawai", "cost", 6))


# five = 5
# three = 3
# print(five % three) # dzielenie modulo, reszta z dzielenia
# print(float("inf")) # zapytanie o liczbę nieskonczoności
# print(float("inf") > 99999999999999)
# print(-float("inf"))

# name = "Justynka"
# wiek = 23
# cos = 365
# print ("%s is %d years old, so is about %d days old" % (name, wiek, cos))
# message = '{0:s} is {1:d} years old, so is about {2:d} days old'
# print(message.format("Justynka", 23, 365))
# wiadomosc = "{0:s} is {1:d} years old, so is about {2:d} days old "
# print(wiadomosc.format("Jaroslaw", 24, 350))
#
# liczba1 = 1234567890
# liczba2 = 12345
# liczba3 = liczba1//liczba2 # dzielenie i pojazanie tylk calosci
# liczba4 = liczba1%liczba2 # dzielenie i pokazanie reszty
# print(liczba3)
# print(liczba4)
#
# # swiatla na trybie automatycznym
# isAutomaticMode = True
# print("isAutomaticMode =", isAutomaticMode)
# # zapalone swiatlo w ciagu dnia
# is80PercentLight = True
# print("is80PercentLight =", is80PercentLight)
# # slonce swieci w oczy kierowcy i swiatlo powinno sie wlaczyc
# isDirectLight = False
# print("isDirectLight =", isDirectLight)
# # mgla, deszcz lub inne niesprzyjajace warunki
# isRainy = True
# print("isRainy =", isRainy)
# #
# swiatla_wlaczone = isAutomaticMode and (is80PercentLight or isDirectLight or isRainy)
# print ("swiatla wlaczone: ", swiatla_wlaczone)
#
# jest_weekend = True
# print("jest_weekend =", jest_weekend)
# pogoda = 19
# print("pogoda =", pogoda)
# dodatkowe_zadania = ""
# print("dodatkowe_zadania = ", dodatkowe_zadania)
#
# zadowolenie = jest_weekend and pogoda >= 15 and dodatkowe_zadania == ""
# print(zadowolenie)
#
# niezadowolenie = not jest_weekend and pogoda < 20 and dodatkowe_zadania != "" \
#                  or not jest_weekend and pogoda <= 20 and dodatkowe_zadania ==""

#
# print(niezadowolenie)

#
# drzewo = "dab"
# print("dab is", type(drzewo))
# liczba = 8
# print("liczba is", type(liczba))
# druga = 7.8
# print("druga is", type(druga))
# print("dwie zmienne is", type(liczba * druga))
#
#
# a=1
# d=1
# f=1
# print(a,d,f, sep="\\")
#
# g=h=r=2
# print(g,h,r, sep="/")
# r=3
# print(g,h,r, sep="\\")
#
# v1 = 126
# print("v1 ma wartosc", type(v1))
# v2 = '126'
# print("v2 ma wartosc", type(v2))
# v3 = 126.0
# print("v3 ma wartosc", type(v3))
# v4 = '126.0'
# print("v4 ma wartosc", type(v4))
# print(v1 * v3)
# print (int(v2) * float(v4))
# print(7 - 1 * 0 + 3 + 3)
# print(4**5 / 2**3) #potegowanie
# print(90+9/9)





# napis = "Dzisiaj mamy hujowy dzien"
# print(napis[0]) #co znajduje sie na tej pozycji
# print(napis[3:7]) # od do
# print(napis[:8]) # do
# print(napis[8:]) # od
# print(napis.find("h")) # zwraca na jakiej pozycji jest to czego szukam
# print(napis.rfind("h")) # zwrana na jakiej pozycji jest to czego chce ale od tylu
# cos = "Nie ma to jak w 'miekkim lozku' samotnie lezec: o poranku"
# print(cos[cos.find(":")+2:])
# cos_znowu = cos[cos.find("'")+1:]
# print(cos_znowu[:cos_znowu.find("'")])
#
# q = "THE EYES"
# print(q[0],q[1],q[2],q[5],q[3],q[7],q[4],q[6])
# z = "a gentleman"
# print(z[3],z[6],z[7],z[2],z[0],z[4],z[5],z[1],z[8:])
#
# program = "Program 'Kropka nad i' nadamy o: 22:00"
# nazwa_programu = program[program.find("'")+1:]
# print(nazwa_programu[:nazwa_programu.find("'")])
# print(nazwa_programu[nazwa_programu.find(":")+2:])
#
# program = 'Program "Pytanie na śniadanie" nadamy o: 6:00'
# print("Program zaczyna się o ", program[program.find(":")+2:])
# nazwa = program[program.find('"')+1:]
# print("Nazwa programu to:", nazwa[:nazwa.find('"')])

#
# print(((38 * 5 + 50) *20 + 1019) - 1995)
# print((9 *2 + 10) / 2 - 9)
#
# zaliczony_semestr = 0.85
# srednia = 3.0
# praca = "nie.zal"
# koncowy_wynik = True
# print(koncowy_wynik and ((zaliczony_semestr > 0.80 and srednia >= 3.0) or praca == "zal"))


'''Lista to zbiór elementów zapisanych pod jedną nazwą zmiennej'''
# lista = ["waz", "malpa", "kot", "pies"]
# print(lista [1]) # wypisanie jednego konkretnego elementu z listy
# lista[1] = "kogut" # zamiana wybranego elementu w liscie
# print(lista)
# lista.append("szczur") # dodawanie kolejnego, nowego elementu do listy na koniec
# print(lista)
# lista.insert(0, "myszka") # dodanie kolejnego, nowego elementu, na miejsce, ktore ja chce
# print(lista)
# lista.remove("kot") # usuwanie z listy konkretnego elementu
# print(lista)
# lista.sort() # sortowanie na liscie
# print(lista)
# lista.pop(2) # usuwanie z listy wybranego elementu
# print(lista)
# lista.index("waz") # sprawdza czy dany element wystepuje na mojej liscie, a jesli tak to na ktorej pozycji
# print(lista.index("waz"))
# print(lista.count("waz")) # sprawdza ile razy w liscie wystepuje dany element
# nowa_lista = ["kukulka", "byk"]
# lista.extend(nowa_lista) # dodanie jednej listy do drugiej
# print(lista)
# nastepna_lista = lista.copy() # kopiowanie listy
# print(nastepna_lista)
# nastepna_lista.clear()
# print(nastepna_lista)
# print(lista)
# kolejna_lista = lista
# kolejna_lista.clear() # czysci liste
# print(kolejna_lista)
# print(lista)
# lista.reverse()  # przepisanie listy od koncz

#
# hity = ["BROTHERS IN ARMS","BOHEMIAN RHAPSODY",'STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
# print(hity)
# hity.append('CHILD IN TIME')
# hity.append('AGAIN')
# print(hity)
# hity.insert(2, 'HOTEL CALIFORNIA')
# print(hity)
# hity.insert(0, 'THE SOUND OF SILENCE')
# print(hity)
# print(hity.index('HOTEL CALIFORNIA'))
# hity.remove('HOTEL CALIFORNIA')
# print(hity)
# hity[0] = 'ENJOY THE SILENCE'
# print(hity)
# kopia_hitow = hity.copy()
# kopia_hitow.reverse()
# print(kopia_hitow)
# kopia_hitow.sort()
# print(kopia_hitow)
# kopia_hitow.pop(0)
# kopia_hitow.pop(0)
# print(kopia_hitow)
# lista_sluchaczy = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']
# kopia_hitow = kopia_hitow + lista_sluchaczy
# print(kopia_hitow)
# print(kopia_hitow.index('WISH YOU WERE HERE'))
# print(kopia_hitow.index('RIDERS ON THE STORM'))
# kopia_hitow.clear()
# print(kopia_hitow)
#
# krotka = (2, 3, 4, 5) # rozni sie od tablicy nawiasami
# print(krotka)
# print(krotka[2]) # odwolanie sie do konkretnego elementu
# print(krotka.index(4)) # na ktrej pozycji sie znajduje konkretny element
# print(krotka.count(4)) # ile razy występuje konkretny element
# print(max(krotka)) # maksymalna wartosc
# krotkaList = list(krotka) #zrobienie z krotki listy
# print(krotkaList)
# krotkaList.append(9)
# nowa_krotka = tuple(krotkaList) # tupple robi nowa stala liste
# print(nowa_krotka)
#
#
# marketing = ["papier", "dlugopis", "olowek"]
# print(marketing)
# marketing.append("pioro")
# print(marketing)
# print(marketing[2])
# marketing.insert(1, "gumka")
# print(marketing)
# Emarketing = marketing.copy()
# print(Emarketing)
# Emarketing.sort()
# print(Emarketing)
# marketingE = ["nozyczki"]
# Emarketing.extend(marketingE)
# nic = tuple(Emarketing) # robienie z listy krodki
# print(Emarketing)
# print(nic)
#
# ### SLOWNIK###
# zadgadka = {"1": "nowy", "2" : "zmija"} # sa dwa elementy majace po dwa skladniki
# print(zadgadka)
# print(zadgadka["2"])
# zadgadka["3"] = "krowa" # dodaje nowy element
# print(zadgadka)
# # print(zadgadka.keys()) # klucze
# # print(zadgadka.values()) # wartosci
# # print(zadgadka.items()) # kolekcja
# # print(zadgadka.popitem()) # usuwa
# print(zadgadka.setdefault("4", "kilo")) # zapytanie sie o cos, wyswietla wartosc i dodaje nowy element
# print(zadgadka)
# print(zadgadka.get("6")) # zapytwanie sie o cos
# nowe_zadgadta = {"2" : "koc", "5" : "biorko"}
# zadgadka.update(nowe_zadgadta) # ZAKTUALIZOWANIE dodanie nowych pojec do slownika, jesli  cos sie powtarza to stare zostaje zamienione na nowe
# print(zadgadka)
#
# kanaly = {"Google" : "1480", "Email" : "300", "Natural Traffic" : "440", "TV Spot" : "700"}
# print(kanaly)
# print(kanaly["Email"])
# nowe_kanaly = {"Natural Traffic" : "520", "News" : "600"}
# kanaly.update(nowe_kanaly)
# print(kanaly)
# print(kanaly.pop("Email")) # usunięcie jednego elementu
# print(kanaly)
#
#
# wiek = 24
# jest_pijany = False
# restrykcja = False
# if wiek >= 18 and not jest_pijany and not restrykcja:
#     print("Możesz kupi alkohol")
# else:
#     print("Nie możesz kupi alkoholu")

#
# like = 500
# udostepnienia = 100
# if like >= 500 and udostepnienia >= 100:
#     print("Obnizka - 10%")
# else:
#     print("Ceny takie same")
#
#
# kupiona_pizza = True
# kupiony_napoj = False
# czy_jest_weekend = False
# if (kupiona_pizza or kupiony_napoj) and not czy_jest_weekend:
#     print("Otrzymujesz darmowego burgera")
# else:
#     print("Dziekujemy za zakupy i zapraszamy ponownie")
#
#
# wielkosc_dysku = 150
# ilosc_zajetego_miejsca = 133
# wielkosc_pliku = 1
#
# if wielkosc_dysku >= ilosc_zajetego_miejsca + wielkosc_pliku:
#     print("plik moze zostac pobrany")
# else:
#     print("nie mozna pobrac pliku, za malo miejsca na dysku")



# wiek = 18
# jest_pijany = True
# restrykcja = False
#
# if wiek < 18:
#     print("Jestes zbyt mlody aby kupic alkohol")
# elif jest_pijany:
#     print("W tym stanie nie mozemy sprzedac ci alkoholu")
# elif restrykcja:
#     print("W tym miejscu nie mozna kupic alkoholu")
# else:
#     print("Mozesz kupic alkohol")
#
#
# like = 500
# udostepnienia = 100
# if like < 500:
#     print("Za malo 'LIKE'")
# elif udostepnienia < 100:
#     print("Za malo udostepnien")
# else:
#     print("Obnizka -10%")
#
#
# kupiona_pizza = False
# kupiony_napoj = True
# czy_jest_weekend = False
# if czy_jest_weekend:
#     print("Promocja dotyczy dni roboczych")
# elif not kupiony_napoj and not kupiona_pizza:
#     print("Brak pizzy lub napoju na rachunku do promocji")
# else:
#     print("Otrzymujesz darmowego burgena")
#
#
# itRains = False
# if itRains:
#     print("We stay at home")
# else:
#     print("We go out")
#
# print("We stay at home" if itRains else "We go out")
#
#
#
# musclePain = False
# fever = False
# weakness = True
#
# print("suspiction of influenza" if musclePain and fever and weakness else "The flu is unlikely")
#
# if musclePain and fever and weakness:
#     print("suspiction of influenza")
# elif weakness and (not musclePain and not fever):
#     print("Just take a rest!")
# else:
#     print("You may by cold")
#
#
# musclePain = False
# fever = False
# weakness = False
# isMan = False
# if musclePain and fever and weakness:
#     print("suspiction of influenza")
# elif isMan and (musclePain or fever or weakness):
#     print("suspiction of influenza")
# elif weakness and (not musclePain and not fever):
#     print("Just take a rest!")
# else:
#     print("You may by cold")
#
#
# check_is_completed = False
# print("check is completed" if check_is_completed else "check not done yet!")
#


#
#
# i = 1
# imax = 10
# # while i <= imax:
# #     print(imax - i, "I like python")
# #     i+=1
# #     if imax - i == 0:
# #         break
#
# while i <= imax:
#     print(i, "I like python")
#     i+=1
# else:
#     print("Now i = ", i)
#
# j = 10
# jmin = 1
# while j >= jmin:
#     print(j, "I like python")
#     j-=1
# else:
#     print("Now j =", j)
# #
#
# firstRow = 1
# lastRow = 31
# currentRow = firstRow
# while currentRow <= lastRow:
#     print("Row number ", currentRow)
#     currentRow +=1
#
#
#
# liczba = 1
# zakres = 13
# while liczba <=zakres:
#     print(liczba,"\t",  liczba**2, "\t", liczba**3)
#     liczba+=1
#
#
#
# number = 2
# potega  = 0
# widelki = 16
# while potega <= widelki:
#     print("2 do potegi ",potega, "to", 2 ** potega)
#     potega+=1



# liczba = 1
# zakres = 10
# while liczba <= zakres:
#     print("x" * liczba)
#     liczba+=1
#
#
# '''odszukanie 3 liczb pod rzad, ktore sa rosnace'''
# values = [10, 43, 12, 48, 12, 11, 18, 97, 57, 28, 19, 27, 47, 19, 74]
# i = 0
# max = len(values) - 2
#
# while i < max:
#     print(i, values[i], values[i + 1], values[i + 2])
#     i+=1
#     if values[i] < values [i + 1] and values[i + 1] < values[i + 2]:
#         print("\tFound: ", values[i], values[i + 1], values[i + 2])




# numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
# j = 0
# max = len(numbers) -1
# while j < max:
#     print(numbers[j], numbers[j + 1])
#     j+=1
#     if numbers[j + 1] ==  numbers[j] ** 2:
#         print("\t Found:", numbers[j], numbers[j + 1])



# numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
# c = 0
# max = len(numbers) - 2
# while c < max:
#     print(numbers[c], numbers[c + 1], numbers [c + 2])
#     c+=1
#     if numbers[c] ** 2 == numbers [c + 1] and numbers [c + 1] **2 == numbers [c + 2]:
#         print("\t Found: ", numbers[c], numbers[c + 1], numbers [c + 2])


# texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# k = 0
# max = len(texts) - 1
# while k < max:
#     print(texts[k], texts[k + 1])
#
#     if len(texts[k]) == len(texts[k + 1]):
#         print("\t Napisy: ", texts[k], texts[k + 1])
#     k += 1


# cargo = [ 40, 20, 4, 5, 30, 8, 2, 7, 3, 19, 32, 40, 20, 35, 15, 32, 9]
# cargo.sort()
# cargo.reverse()
# print(cargo)
# boxCapacity = 90
# box = []
# i = 0
# while i < len(cargo) and (boxCapacity - sum(box) >= min(cargo)):
#     if (boxCapacity - sum(box)) >= cargo[i]:
#         box.append(cargo[i])
#     i+=1
# print("The collect items sum is:", sum(box))
# print("The elements are: ", box)


# number = -1
# numberx = 0
# while number < 50:
#     number+=1
#     print(number, "+", number +1, "=", number + number+1)



# import random
# my_number = random.randint(0, 10)
# guess = 2
# ile_razy = []
# print(my_number)
# while guess != my_number:
#     if my_number > guess:
#         print("PODAJ MNIEJSZA LICZBE")
#         ile_razy.append(my_number)
#         my_number = random.randint(0, 10)
#     elif my_number < guess:
#         print("PODAJ WIEKSZA LICZBE")
#         ile_razy.append(my_number)
#         my_number = random.randint(0, 10)
#
# print("GRATULACJE, probowales: ", len(ile_razy) + 1)



# import random
# my_number = random.randint(0, 10)
# guess = 2
# ile_razy = 0
# print(my_number)
# while  guess != my_number:
#     if my_number > guess:
#         print("PODAJ MNIEJSZA LICZBE")
#         ile_razy+=1
#         my_number = random.randint(0, my_number)
#     elif my_number < guess:
#         print("PODAJ WIEKSZA LICZBE")
#         ile_razy+=1
#         my_number = random.randint (my_number, 10)
#
# print("GRATULACJE, prubowales: ", ile_razy + 1)





# import random
# my_number = random.randint(0, 50)
# zuzyte = []
# guess = 2
# ile_razy = 0
# print("liczba do odgadniecia: ", guess)
# while  guess != my_number:
#     if my_number > guess and my_number not in zuzyte:
#         print("PODAJ MNIEJSZA LICZBE")
#         zuzyte.append(my_number)
#         ile_razy+=1
#         my_number = random.randint(0, my_number)
#     elif my_number < guess and my_number not in zuzyte:
#         print("PODAJ WIEKSZA LICZBE")
#         zuzyte.append(my_number)
#         ile_razy+=1
#         my_number = random.randint (my_number, 50)
#     else:
#         my_number = random.randint(0, 50)
#
# print("GRATULACJE, prubowales: ", ile_razy + 1)
# print(zuzyte)




# imiona = ["Kinga", "Zofia", "Kamila", "Szymon", "Kuba", "Marian", "Waldek"]
# mail = "mojtowarzysz.com"
# for imie in imiona:
#      email = imie + "@" + mail
#      print("Adres email dla\t", imie, "to", email)
# else:
#     print("Koniec listy")



# data = ['Error: File cannot be open',
#         'Error: No free space on disk',
#         'Error: File missing',
#         'Warning: Internet connection lost',
#         'Error: Access denied']
# for format in data:
#     print(format.upper())
#
# for element in data:
#     elements1 = element.split(":")
#     print(elements1[0].upper())
#     print(elements1[1])

#
# elements1 = []
#
# for element in data:
#     elements1 = element.split(":")
#     if elements1[0] == "Error":
#         print(elements1[1].upper())
#     else:
#         print(elements1[1])


# for number in range(1, 21, 2): # trzeci parametr mowi co ile sie bedziemy przesuwac w zakresie range
#     print(number)
#
#
# for number in range(1, 21):
#     if number % 2 ==0:
#         print(number, "- liczba parzysta")
#     else:
#         print(number, "- liczba nieparzysta")


# string_A = '+---+---+---+---+'
# string_B = '|   |   |   |   |'
#
# for stringA in range(10):
#     print(string_A)
#
#
# for string in range(10):
#     if string % 2 == 0:
#         print(string_A)
#     else:
#         print(string_B)
#
#
#
#
#
# znak = "x"
# for znaczek in range(10):
#     if znaczek % 2 == 0:
#         print(znak * znaczek)
#     else:
#         print(znaczek * znak)



# znak1 = "o"
# znak2 = "x"
# for znaczek in range(10):
#     if znaczek % 2 == 0:
#         print(znak1 * znaczek)
#     else:
#         print(znak2 * znaczek)

# '''Tabliczka mnożenia'''
# for x in range(1, 11):
#     line = str(x)
#     for y in range(1, 11):
#         line += "%3d" % (x * y)
#     print(line)


# for x in range(11):
#     for y in range(11):
#         print(x, "*", y, "=", x * y)
#
#
#

# for x in range(11):
#     line = str(x)  # linijka tekstu dla tego wiersza
#     for y in range(11):
#         line += ("\t%3d" %(x*y))
#     print(line)


#
# i = 10
# j = 1
# for x in range (1, 11):
#     j *= x
# print(i, j)


# x = 10
# result = 1
# for i in range(1, x + 1):
#     for j in range(1, i + 1):
#         result *= j
#     print(i, result)
#     result = 1


# list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
# list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']
#
# for y in list_noun:
#     for p in  list_adj:
#         print(y, p)



# for liczba_pierwsza in range(2,31):
#     for x in range(2, liczba_pierwsza):
#         if liczba_pierwsza % x == 0:
#             print("liczba", liczba_pierwsza, "nie jest liczbą pierwsza - ", x)
#             break
#     else:
#         print("%2d jest liczba pierwsza!!!" % (liczba_pierwsza))



#
# text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.'
# short_text = ''
# words = text.split(' ')
# counter = 0
# for word in words:
#     short_text += word + ' '
#     counter += 1
#     if counter >= 20:
#         print(short_text)
#         break
#
#
#
# definitions = [
#     'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.',
#     'Ein Kraftwandler ist eine mechanische Anordnung zur Veränderung einer Kraft in Bezug auf ihren Angriffspunkt, ihre Richtung oder ihren Betrag. Die einfachsten Kraftwandler sind Seile, Stangen, Rollen, schiefe Ebenen und Hebel. Dies sind gleichzeitig die grundlegenden einfachen Maschinen.',
#     'La ventaja mecánica es una magnitud adimensional que indica cuánto se amplifica la fuerza aplicada usando un mecanismo (ya sea una máquina simple, una herramienta o un dispositivo mecánico más complejo) para contrarrestar una carga de resistencia.',
#     'Cette notion s\'applique de manière évidente dans les systèmes de poulies et de leviers. Elle est centrale dans les systèmes de freinage : on applique une petite force sur un parcours important et l\'on obtient une force importante transmise au système de freinage pour une course de faible distance.'
#     ]
#
# for definition in definitions:
#     words = definition.split(' ')
#     short_text = ''
#     counter = 0
#     for word in words:
#         short_text += word + ' '
#         counter += 1
#         if counter >= 20:
#             print(short_text)
#             break




# persons = ["Justyna", "Jaroslaw", "Julia@gmail.com", "Ela", "Antek", "Sylwia@gmail.com"]
# dodatek = "@gmail.com"
# czlonkowie = []
# # for osoba in persons:
# #     if "@" in osoba:
# #         czlonkowie.append(osoba)
# #     else:
# #         mail = osoba + dodatek
# #         czlonkowie.append(mail)
# # print(czlonkowie)
#
# for osoba in persons:
#     if "@" in osoba:
#         czlonkowie.append(osoba)
#         continue
#     mail = osoba + dodatek
#     czlonkowie.append(mail)
# print(czlonkowie)
#
# menu = '''
# Choose what you want me to do for you:
# 1 - COFFEE
# 2 - TEA
# 3 - MAKE ME SMILE
# ---------------
# To stop this script select 0
# '''
#
# smile = '''
#
#                           oooo$$$$$$$$$$$$oooo
#                       oo$$$$$$$$$$$$$$$$$$$$$$$$o
#                    oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
#    o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
# oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
# "$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
#   $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
#   $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
#    "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
#     $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
#    o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
#    $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
#   o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
#   $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
#  """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
#             "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
#               $$$o          "$$""$$$$$$""""           o$$$
#                $$$$o                                o$$$"
#                 "$$$$o      o$$$$$$o"$$$$o        o$$$$
#                   "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
#                      ""$$$$$oooo  "$$$o$$$$$$$$$"""
#                         ""$$$$$$$oo $$$$$$$$$$
#                                 """"$$$$$$$$$$$
#                                     $$$$$$$$$$$$
#                                      $$$$$$$$$$"
#                                       "$$$""""
# '''
#
# while True:
#     print(menu)
#     letter = input("wybierz cos: ")
#     if letter == "1":
#         print("Function COFFEE not implemented")
#         input("press enter")
#         continue
#     elif letter == "2":
#         print("Function TEA not implemented")
#         input("press enter")
#         continue
#     elif letter == "3":
#         print(smile)
#         input("press enter")
#         continue
#     elif letter == "0":
#         break
#     else:
#         print("You need to make a valid choice. Press ENTER and try again!")
#         input("press enter")



# initialCapital = 20000
# procent = 0.03
# maxTimeYears = 10
# zmienna = 0
#
# for x in range(10):
#     zysk = initialCapital * procent
#     initialCapital = initialCapital + zysk
#     print("twoj procent na rok to %d a stan konta wynosi %d" % (zysk, initialCapital))

# while zmienna < maxTimeYears:
#     zysk = initialCapital * procent
#     initialCapital = initialCapital + zysk
#     print("twoj procent na rok to %d a stan konta wynosi %d" % (zysk, initialCapital))
#     zmienna +=1

# number = 20730906
# suma = 0
# while number > 0:
#     reszta = number % 10
#     number = number // 10
#     suma += reszta
# print(suma)




# text = '''United Space Alliance: This company provides major support to NASA for
# various projects, such as the space shuttle. One of its projects is to
# create Workflow Automation System (WAS), an application designed to
# manage NASA and other third-party projects. The setup uses a central
# Oracle database as a repository for information. Python was chosen over
# languages such as Java and C++ because it provides dynamic typing and
# pseudo-code–like syntax and it has an interpreter. The result is that
# the application is developed faster, and unit testing each piece is easier.'''
#
# x = 0
# slowo_dluzsze_o_6 = 0
# tablica_slow = text.split(" ")
# # while x < len(tablica_slow):
# #     if len(tablica_slow[x]) >= 6:
# #         slowo_dluzsze_o_6 +=1
# #     x += 1
# # print(slowo_dluzsze_o_6)
#
#
# for slowo in tablica_slow:
#     if len(slowo) >= 6:
#         slowo_dluzsze_o_6 +=1
# print(slowo_dluzsze_o_6)



# a1 = 0
# a2 = 1
# a3 = 0
# fib = 20
# # for x in range(1, 21):
# #     a3 = a1 + a2
# #     a1 = a2
# #     a2 = a3
# # print(a3)
#
# x = 1
# while x <= fib:
#     a3 = a1 + a2
#     a1 = a2
#     a2 = a3
#     x+=1
# print(a3)


# text ='''Industrial Light & Magic: In this case, you find Python
# used in the production process for scripting complex,
# computer graphic-intensive films. Originally, Industrial
# Light & Magic relied on Unix shell scripting, but it was
# found that this solution just couldn’t do the job. Python
# was compared to other languages, such as Tcl and Perl, and
# chosen because it’s an easier-to-learn language that the
# organization can implement incrementally. In addition, Python
# can be embedded within a larger software system as a scripting
# language, even if the system is written in a language such as
# C/C++. It turns out that Python can successfully interact with
# these other languages in situations in which some languages can’t.'''
# wyrazy = text.lower().split(" ")
# suma = 0
# x = 0
# while x < len(wyrazy):
#     if wyrazy[x].count("p") != 0:
#         suma += 1
#     x += 1
# print(suma)

# dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less then 50%'}
# print(dictionary)
# for x in dictionary.items():
#     print(x[0], "-", x[1])

# text = '''Industrial Light & Magic: In this case, you find Python
# used in the production process for scripting complex,
# computer graphic-intensive films. Originally, Industrial
# Light & Magic relied on Unix shell scripting, but it was
# found that this solution just couldn’t do the job. Python
# was compared to other languages, such as Tcl and Perl, and
# chosen because it’s an easier-to-learn language that the
# organization can implement incrementally. In addition, Python
# can be embedded within a larger software system as a scripting
# language, even if the system is written in a language such as
# C/C++. It turns out that Python can successfully interact with
# these other languages in situations in which some languages can’t.'''
#
# slownik = {}
# lista = text.split(" ")
# for slowo in lista:
#     if slowo not in slownik.keys():
#         slownik[slowo] = 1
#     else:
#         slownik[slowo] +=1
# print(slownik)



# f_smaller = 3.14928303984727364
# f_bigger = 3.8773625392
# print(f_smaller,"\t", f_bigger)
# print(int(f_smaller), "\t", int(f_bigger)) # pozostawia same calosci
# print(abs(f_smaller), "\t", abs(-f_smaller)) # wartosc bezwzgledna, zawsze zwraca liczbe dodatnia
# print(round(f_smaller, 2), "\t", round(f_smaller, 3), "\t", round(f_smaller)) # zaokragla wartosc po przecinku, trzeba napisac ile miejsc
# print(min(f_smaller, f_bigger), "\t", max(f_bigger, f_smaller)) # wyciąga z kilku wartosci, wartosc najwieksza lub najmniejsza
# lista = [1, 2, 3, 4, 5, 4, 4, 5, 4]
# print(sum(lista)) # suma elementow w tablicy
# print(len(lista)) # dlugosc listy
# print(sum(lista) / len(lista)) # wyliczenie sredniej w liscie
# print(round(2.645, 2))




# percent = [2.606255012, 1.222935044, 1.283079391, 3.628708901, 6.856455493, 4.911788292,
#            2.886928629, 0.781876504, 0.962309543, 2.265437049, 6.816359262, 3.688853248,
#            3.468323978, 5.633520449, 4.530874098, 1.984763432, 0.922213312, 3.327987169,
#            4.190056135, 5.493183641, 1.864474739, 10.60545309, 2.425821973, 2.726543705,
#            8.740978348, 6.174819567]
#
# countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
#              'Norway', 'Portugal', 'United Kingdom', 'Serbia', 'Germany', 'Albania',
#              'France', 'Czech Republic', 'Denmark', 'Australia', 'Finland', 'Bulgaria',
#              'Moldova', 'Sweden', 'Hungary', 'Israel', 'Netherlands', 'Ireland',
#              'Cyprus', 'Italy']
# sumOfPoints = 4988
# print(sum(percent))
# print(max(percent))
# print(min(percent))
# for x in range(len(countries)):
#     print(percent[x], int(percent[x]), round(percent[x], 2), int(round(percent[x] * sumOfPoints / 100, 0)), countries[x])



# import math # importowanie zmiennej math
# print(math.pi)
# from math import * # importowanie zmiennej math ale inna metoda
# print(pi)
# print(floor(pi)) # zaokraglilo liczbe pi
#
# percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
#
#            2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
#
#            3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
#
#            4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
#
#            8.740978348,6.174819567]
# import statistics
# print(statistics.median(percent), statistics.median_low(percent),  statistics.median_high(percent)) # obliczanie median
# import math
# from statistics import *
# print(median(percent), median_low(percent), median_high(percent))

# f_smaller = 3.14928303984727364
# f_bigger = 3.8773625392
# import math
# print(math.ceil(f_smaller), math.ceil(f_bigger)) # wyswietla najmniejsza liczbe calkowita wieksza od danej
# print(math.floor(f_smaller), math.floor(f_bigger)) # wyswietla najwieksza liczbe calkowita z mniejszych od danej
# print(math.ceil(-f_smaller), math.ceil(-f_bigger))
# print(math.floor(-f_smaller), math.floor(-f_bigger))
# print(pow(2,8), pow(0, 0.5)) # pierwszy argument mowi o liczbie a drugi o potedze do ktorej chcemy podniesc dana liczbe
# print(math.sqrt(16)) # zwraca licze, ktora jest jest podniesiona do kwadratu
# print(math.pi, math.e) # sa to stale
# print(math.sin(math.pi/2), math.cos(math.pi/4))# zawiera rozne funkcje np. trugonometryczne



# import math
# # 1° = (π * rad)/180
# # 1 rad = 180°/π

# degree = 360
# print((math.pi * 360) / 180, math.radians(360))
# print((math.pi * 45) / 180, math.radians(45))
#
#
# # small - promień 22 cm, cena, 11.50
# #
# # big - promień 27 cm, cena 15.60
# #
# # family - promień 38cm, cena 22.00
#
#
# pizza_r = 22
# big_pizza_r = 27
# family_pizza_r  = 38
# small_pizza_price = 11.50
# big_pizza_price = 15.60
# family_pizza_price = 22.00
#
# print((math.pi * pizza_r ** 2) / 100)
# print((math.pi * big_pizza_r ** 2) / 100)
# print((math.pi * family_pizza_r ** 2) / 100)
#
# print(11.50 / (math.pi * pizza_r ** 2) / 100)
# print(15.60 / (math.pi * big_pizza_r ** 2) / 100)
# print(22.00 / (math.pi * family_pizza_r ** 2) / 100)




# import random
# print("One random number: ", random.randint(1,100)) # losuje liczby calkowite od 1 do 100
# print("Wybrany element z listy: ", random.choice(range(1, 100))) # może wybrac losowy element nawet z listy
# print("Wybrano z zakresu: ", random.randrange(1, 100)) # oznacza to samo co na gorze
# imiona = ["Kinga", "Zofia", "Kamila", "Szymon", "Kuba", "Marian", "Waldek"]
# random.shuffle(imiona)
# print("Wylosowano z listy imion:", imiona) # losuje slowa z listy
# print("Losowanie liczby:", random.random()) # losuje liczbe typu float od 0 do 1



# import random
# x=1
# while x < 11:
#     print(x, "liczba randomowa to", random.randint(1,100))
#     x+=1


# import random
# number1 = random.randint(1, 100)
# print("Liczba do odgadniecia to: %s " % (number1))
# number2 = random.randint(1, 100)
# counter = 1
# ilosc = 0
# while number1 != number2:
#     if number1 != number2:
#         ilosc +=1
#         number2 = random.randint(1, 100)
#     else:
#         break
# print(number1, number2, "ilosc prob:", ilosc + 1)


#
# import random
# countries = [
#     'Uruguay',
#     'Russia',
#     'Saudi Arabia',
#     'Egypt',
#     'Spain',
#     'Portugal',
#     'Iran',
#     'Morocco',
#     'France',
#     'Denmark',
#     'Peru',
#     'Australia',
#     'Croatia',
#     'Argentina',
#     'Nigeria',
#     'Iceland',
#     'Brazil',
#     'Switzerland',
#     'Serbia',
#     'Costa Rica',
#     'Sweden',
#     'Mexico',
#     'Korea Republic',
#     'Germany',
#     'Belgium',
#     'England',
#     'Tunisia',
#     'Panama',
#     'Colombia',
#     'Japan',
#     'Senegal',
#     'Poland'
#     ]


# random.shuffle(countries)
# x=0
# while x <len(countries) :
#     if x % 2 == 0:
#     print(countries[x], "---", countries[x + 1])
#     x+=1



# random.shuffle(countries)
# x = 0
# while x < len(countries):
#     if x % 4 == 0:
#         print("---GRUPA X ---")
#         print(countries[x])
#         x+=1
#     else:
#         print(countries[x])
#         x+=1
#
#
# random.shuffle(countries)
# groupNumbe = 0
# x = 0
# while x < len(countries):
#     if x % 4 == 0:
#         print("---GRUPA X ---")
#     print(countries[x])
#     x+=1


# '''WYSWIETLENIE TABELI ASCII
# posiada ona 256 znakow i kazdy z nich ma swoja numeryczna reprezentacje'''
# for i in range(32, 127):
#     print(i, chr(i))



# import random
# ints = range(33, 127)
# password = ""
# for i in range(16):
#     password += chr(random.choice(ints))
# print("Password is: ", password)


# import random
# i = random.randint(1, 6)
# print(i)
# if i == 1:
#     print("")
#     print("o")
#     print("")
#
# elif i == 2:
#     print("  o")
#     print("")
#     print("o")
#
# elif i == 3:
#     print("  o")
#     print(" o")
#     print("o")
#
# elif i == 4:
#     print("o  o")
#     print("")
#     print("o  o")
#
# elif i == 5:
#     print("o   o")
#     print("  o")
#     print("o   o")
#
# else:
#     print("o   o")
#     print("o   o")
#     print("o   o")







# import random
# i = random.randint(1, 6)
# y = 1
# print("WITAMY W GRZE")
# while y <=5:
#     if i == 1:
#         print("rzut: ", y)
#         print("")
#         print("o")
#         print("")
#         i = random.randint(1, 6)
#         y += 1
#     elif i == 2:
#         print("rzut: ", y)
#         print("  o")
#         print("")
#         print("o")
#         i = random.randint(1, 6)
#         y += 1
#     elif i == 3:
#         print("rzut: ", y)
#         print("  o")
#         print(" o")
#         print("o")
#         i = random.randint(1, 6)
#         y += 1
#     elif i == 4:
#         print("rzut: ", y)
#         print("o  o")
#         print("")
#         print("o  o")
#         i = random.randint(1, 6)
#         y += 1
#     elif i == 5:
#         print("rzut: ", y)
#         print("o   o")
#         print("  o")
#         print("o   o")
#         i = random.randint(1, 6)
#         y += 1
#     else:
#         print("rzut: ", y)
#         print("o   o")
#         print("o   o")
#         print("o   o")
#         i = random.randint(1,6)
#         y += 1
# print("KONIEC GRY")

# line = "this is a very STRANGE text"
# print(line.capitalize()) # przekształca tekst do zdania zaczynającego się wielką literą
# print(line.title()) # każde słowo zaczyna się od dużej litery
# print(line.upper()) # tekst dużymi literami
# print(line.lower()) # tekst malymi literami
# print(line.swapcase()) # zamienia duże literki na małe a małe literki na duże
# print(line.casefold()) # zamienia znaki danego jezyka na uniwersalne np. niemieckie B na ss
# print(line.count("e")) # ile razy wystepowala dana literka
# print(line.find("e")) # na korej pozycji sie znajduje literla idac od strony lewej
# print(line.rfind("e")) # na ktorej pozycji sie znajduje literka idac od strony lewej
# print(line.index("e")) # na działa jak find tylko jesli nie ma danej literki to wywala blad
# print(line.rindex("e")) # dziala jak rfind tylko jesli nie ma danej literki to wywala blad
# print( "e" in line) # zapytanie sie czy coś występuje w danym tekście czy też nie
# print(line.startswith("t")) # czy zaczyna się podaną literką podany tekst
# print(line.endswith("u")) # czy konczy się na podaną literkę dany tekst
# dlugi_trkst = '''Miala baba koguta
# wsadziala go du buta
# SIEDZ''' # jeśli mamy długi tekst to można go zamkną w potrjnym cudzysłowiu
# print(dlugi_trkst)
# import string
# print(string.ascii_letters) # odpowiedzialny za duże i małe litery
# print(string.digits) # odpowiedzialny za cyfry
# print(line.split(" ")) # rozbija napis
# lista = line.split(" ")
# print(" ".join(lista)) # łączy elementy z tablicy lub wceśniej rozbity tekst





# poem = '''1.Runą i w łunach spłoną pożarnych
# Krzyże kościołów, krzyże ofiarne
# I w bezpowrotnym zgubi się szlaku
# W lechickiej ziemi Orzeł Polaków.
# 2.O, jasne słońce- wodzu Stalinie!
# Niech sława twoja nigdy nie zginie
# Niechaj jak orły powiedzie z gniazda
# Rosja i z Kremla płonąca gwiazda.
# 3.Na ziemskim globie flagi czerwone
# Będą na wiatrach grały jak dzwony
# Czerwona Armia i wódz jej Stalin
# Odwiecznych wrogów na zawsze obali!
# 4.Zaćmisz się rychło w czarnej godzinie
# Polsko- Twe córy i syny,
# Wiara i każdy krzyż na mogile,
# U stóp am legą w prochu i pyle! '''
# potex_x = poem.split("\n")
# print(potex_x)
# #
#
# ''' Napisz pętlę for wyświetlającą liniję pierwszą, dziewiątą, drugą, dziesiątą, trzecią,
# jedenastą itp. Pisząc pętlę for pamiętaj o tym że tak na prawdę mówimy  o linijkach 0,8,1,9,2,10...
#
# '''
#
#
# x = len(potex_x)
# print(x)
# i = 0
# while i < (1/2) * x:
#     print(potex_x[i], potex_x[i + 8])
#     i += 1

#
# lines = poem.split('\n')
# for i in range(8):
#     print(lines[i])
#     print(lines[i+8])


# import time
# print(time.time()) # zwraca czas w sposub yniksowy czyli od 1.23.1970 roku i jest to liczba sekund, ktre upłynęły od tego czasu
# print(time.localtime(time.time())) # pokazuje date i godzine
# print(time.asctime(time.localtime(time.time()))) # pokazuje date i godzine
# print(time.localtime(time.clock()))


# import calendar
# print(calendar.month(2019, 3, w = 6,)) # w = 6 to odstępy
# print(calendar.weekday(1995, 6, 24)) # jaki wtedy był dzień nie ważne czy zmienimy kolejnoś dni w kalendarzu
# calendar.setfirstweekday(6) # 1 dzien w tygodniu to poniedziałek, jeśli chce aby pierwszym dniem tygodnia była niedziela to robie coś takiego, wpływa tylko na to jak kalendarz jest rysowany
# print(calendar.month(2019, 3, w = 6,)) # w = 6 to odstępy
# print(calendar.isleap(2020)) # pyta się czy podany rok jest przestępny
# print(calendar.leapdays(2000, 2020)) # pyta siee ile było dni przestępnych w tych latach ale nie zalicza się do tego ostatni rok
# print(calendar.leapdays(2000, 2021))
# print(calendar.calendar(1995)) # wywołuje cały kalendarz danego roku


# import time
# print(time.localtime(time.time()))
# print(time.asctime(time.localtime(time.time())))
# import calendar
# print(calendar.month(1994, 6, w = 4))
# calendar.setfirstweekday(6)
# print(calendar.month(1995, 6, w = 4))
# print(calendar.isleap(1995))
# print(calendar.calendar(2019))


# import datetime
# print(datetime.MINYEAR, datetime.MAXYEAR) # minimalna i maksymalna wartoś dopuszczalna dla roku
# di = datetime.timedelta(days = 1, hours = 2, minutes = - 30)# służy do liczenia rozncy czasu
# print(di)
# d2 = datetime.timedelta(days = - 1, hours = -7, minutes = - 47) # obliczy ile wcześniej coś się stało
# print(d2)
# print(di + d2)
# print(datetime.date.today()) # zapytanie o dzisiejszą datę
# today = datetime.date.today() # zapamiętuje dzisiajszą datę
# zalegly_czas = datetime.timedelta(days = 7)
# print("today is:", today)
# print("Bills shopul be paid withen", zalegly_czas, "days")
# print("The bills should be paid till", today + zalegly_czas)
# end_of_the_world = datetime.time.max
# print("The final end of world will happen 'by Python'", end_of_the_world)
# born_date = datetime.date(1995, 6, 24)
# print(today - born_date) # wyliczenie ile dni ktoś żyje
# print(datetime.datetime.now()) # dzisiejsza data i godzina
# print(datetime.datetime.today()) # dzisiajsza data i godzina
# print(datetime.datetime.today().weekday()) # zwraca jaki dzisiaj dzien mamy
# print("%a", datetime.datetime.now().strftime("%a"))# konwersuje czas do napisu w skrocie
# print("%A", datetime.datetime.now().strftime("%A"))# konwersuje czas do napisu w pełnej nazwie
# print("%w", datetime.datetime.now().strftime("%w"))# konwersuje czas do napisu ale jako numer dnia tygodnia
# # print("%Y %m %d %H %M %S %f", datetime.datetime.strftime("%Y %m %d %H %M %S %f"))



# import math
# inputdata = [0,1,2,3,5,8,13,21,34,55,89]
# factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]
# print(inputdata)
# print(factortable)
# x = 0
# if len(inputdata) == len(factortable):
#     print("OK")
#     while x < len(inputdata):
#         minvalue = inputdata[x] - factortable[x] * inputdata[x]
#         maxvalue = inputdata[x] + factortable[x] * inputdata[x]
#         mininteger = math.floor(minvalue)
#         maxinteger = math.ceil(maxvalue)
#         print("MIN ", minvalue, "MAX ", maxvalue)
#         print("min ", mininteger, inputdata[x], "max", maxinteger)
#         x += 1
# else:
#     print("inputdata and factortable need to have equal number of elements")






# import random
# import math
# inputdata = [0,1,2,3,5,8,13,21,34,55,89]
# factortable = random.random()
# x = 0
# while x < len(inputdata):
#     minvalue = inputdata[x] - factortable * inputdata[x]
#     maxvalue = inputdata[x] + factortable * inputdata[x]
#     mininteger = math.floor(minvalue)
#     maxinteger = math.ceil(maxvalue)
#     print("MIN ", minvalue, "MAX ", maxvalue)
#     print("min ", mininteger, inputdata[x], "max", maxinteger)
#     factortable = random.random()
#     x += 1



# import datetime
# print(datetime.datetime.now())
# print(datetime.date.today())
# print(datetime.datetime.today().weekday())
# print("%a", datetime.datetime.now().strftime("%a"))
# print("%w", datetime.datetime.now().strftime("%w"))


# import datetime
# print(datetime.datetime.now())
# dzien = int(datetime.datetime.now().strftime("%w"))
# if dzien == 1:
#     print("PONIEDZIAŁEK")
# elif dzien == 2:
#     print("WTOREK")
# elif dzien == 3:
#     print("SRODA")
# elif dzien == 4:
#     print( "CZWARTEK")
# elif dzien == 5:
#     print("PIATEK")
# elif dzien == 6:
#     print( "SOBOTA")
# else:
#     print("NIEDZIELA")






# import random
# myNumbers = []
# while len(myNumbers) < 7:
#     newNumber = random.randint(1, 49)
#     if newNumber in myNumbers:
#         print("Eliminated: ", newNumber)
#         continue
#     myNumbers.append(newNumber)
# print("Those numbers will win: ", myNumbers)





# import random
# colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
# figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']
# allCards = []
#
# for kolor in colors:
#     for figura in figures:
#         karta = kolor + " " + figura
#         allCards.append(karta)
#
# random.shuffle(allCards)
# print(allCards)
# player1 = []
# player2 = []
# x=0
#
# for rozdac in allCards:
#     if x % 2 ==0:
#         player1.append(allCards[x])
#         x += 1
#     else:
#         player2.append(allCards[x])
#         x +=1
# print("Player1: ", player1)
# print("Player2: ", player2)

# for rozdac in allCards:
#     if x < 12:
#         player1.append(rozdac)
#         x += 1
#     else:
#         player2.append(rozdac)
#         x += 1
# print("Player1: ", player1)
# print("Player2: ", player2)


# numbers = [1]
# print(numbers)
# for i in range(5):
#     newNumbers = [1]
#     position = 0
#     while position < len(numbers) - 1:
#         newNumbers.append(numbers[position] + numbers[position + 1])
#         position += 1
#     newNumbers.append(1)
#     numbers = newNumbers.copy()
#     print(numbers)
# # #

# zmienna = 50
# numbers = [1]
# line = ''
# for n in numbers:
#     line += "%3d" % (n)
# print(line.center(zmienna))
#
# for i in range(5):
#     newNumbers = [1]
#     position = 0
#     while position < len(numbers) - 1:
#         newNumbers.append(numbers[position] + numbers[position + 1])
#         position += 1
#
#     newNumbers.append(1)
#     numbers = newNumbers.copy()
#     line = ''
#     for n in numbers:
#         line += "%3d" % (n)
#     print(line.center(zmienna))





#
# colors = ['Hearts','Diamonds','Clubs','Spades']
# figures = [
#     {'Figure':'Ace',  'Power':14},
#     {'Figure':'King', 'Power':13},
#     {'Figure':'Queen','Power':12},
#     {'Figure':'Jack', 'Power':11},
#     {'Figure':'10',   'Power':10},
#     {'Figure':'9',    'Power':9}]
# allCards = []
# #
# for kolor in colors:
#     for figura in figures:
#         aCard = figura.copy()
#         aCard['Color'] = kolor
#         allCards.append(aCard)
# import random
# random.shuffle(allCards)
# print(allCards)
#
# player1 = []
# player2 = []
# x = 0
# for rozdac in allCards:
#     if x % 2 == 0:
#         player1.append(rozdac)
#         x += 1
#     else:
#         player2.append(rozdac)
#         x += 1
# print("Player1: ", player1)
# print("Player2: ", player2)
#
# print(len(allCards))
#
# while 0 < len(player1) and 0 < len(player2):
#     car1 = player1.pop(0)
#     car2 = player2.pop(0)
#
#     print(len(player1))
#     print(len(player2))
#
#     if int(car1["Power"]) == int(car2["Power"]):
#         player1.append(car1)
#         player2.append(car2)
#         print("REMIS: ", car1["Power"], "---", car2["Power"])
#     elif int(car1["Power"]) > int(car2["Power"]):
#         player1.append(car1)
#         player1.append(car2)
#         print("GRACZ I: ", car1["Power"], "---", car2["Power"])
#     else:
#         player2.append(car1)
#         player2.append(car2)
#         print("GRACZ II:", car1["Power"], "---", car2["Power"])
#
# if len(player1) > 0:
#     print('PLAYER 1 WON!!!!')
# else:
#     print('PLAYER 2 WON!!!!')


 ### SLOWNIK###
# zadgadka = {"1": "nowy", "2" : "zmija"} # sa dwa elementy majace po dwa skladniki
# print(zadgadka)
# print(zadgadka["2"])
# zadgadka["3"] = "krowa" # dodaje nowy element
# print(zadgadka)
# # print(zadgadka.keys()) # klucze
# # print(zadgadka.values()) # wartosci
# # print(zadgadka.items()) # kolekcja
# # print(zadgadka.popitem()) # usuwa
# print(zadgadka.setdefault("4", "kilo")) # zapytanie sie o cos, wyswietla wartosc i dodaje nowy element
# print(zadgadka)
# print(zadgadka.get("6")) # zapytwanie sie o cos
# nowe_zadgadta = {"2" : "koc", "5" : "biorko"}
# zadgadka.update(nowe_zadgadta) # ZAKTUALIZOWANIE dodanie nowych pojec do slownika, jesli  cos sie powtarza to stare zostaje zamienione na nowe
# print(zadgadka)




# colors = ['Hearts','Diamonds','Clubs','Spades']
# figures = [
#     {'Figure':'Ace',  'Power':14},
#     {'Figure':'King', 'Power':13},
#     {'Figure':'Queen','Power':12},
#     {'Figure':'Jack', 'Power':11},
#     {'Figure':'10',   'Power':10},
#     {'Figure':'9',    'Power':9}]
# allCards = []
#
# for kolor in colors:
#     for figura in figures:
#         aCard = figura.copy()
#         aCard['Color'] = kolor
#         allCards.append(aCard)
# import random
# random.shuffle(allCards)
# print(allCards)
#
# player1 = []
# player2 = []
# x=0
# for rozdac in allCards:
#     if x % 2 ==0:
#         player1.append(allCards[x])
#         x += 1
#     else:
#         player2.append(allCards[x])
#         x +=1
# print("Player1: ", player1)
# print("Player2: ", player2)
#
#
#
# while 0 < len(player1) and 0 < len(player2):
#
#     car1 = player1.pop(0)
#     car2 = player2.pop(0)
#     stock = []
#     if int(car1["Power"]) == int(car2["Power"]):
#         print("wojna")
#
#         while int(car1["Power"]) == int(car2["Power"]):
#
#             stock.append(car1)
#             stock.append(car2)
#
#             if len(player1) < 3:
#                 player2.append(stock)
#                 stock.clear()
#                 player2.append(player1)
#                 player1.clear()
#                 print("wygrywa gracz II")
#                 break
#             elif len(player2) < 3:
#                 player1.append(stock)
#                 stock.clear()
#                 player1.append(player2)
#                 player2.clear()
#                 print("wygrywa gracz I")
#                 break
#             elif len(player1) >= 3 and len(player2) >= 3:
#                 car1 = player1.pop(0)
#                 car2 = player2.pop(0)
#                 stock.append(car1)
#                 stock.append(car2)
#                 car1 = player1.pop(0)
#                 car2 = player2.pop(0)
#
#
#     elif int(car1["Power"]) > int(car2["Power"]):
#         player1.append(car1)
#         player1.append(car2)
#         print("GRACZ I: ", car1["Power"], "---", car2["Power"])
#
#     elif int(car1["Power"]) < int(car2["Power"]):
#         player2.append(car1)
#         player2.append(car2)
#         print("GRACZ II:", car1["Power"], "---", car2["Power"])
#
#     else:
#         print("koniec gry")
#         break




# def PrintHello():
#     # this functions just prints hello
#     print("Hello")
#     return
#
# PrintHello()



# def PrintCat():
# # this function prints a cat ascii - art
#     text = '''
#        |\---/|
#        | o_o |
#         \_^_/'''
#     print(text)
#     return
# PrintCat()
#
#
# def PrintBear():
# # this function prints a bear ascii - art
#     text = r'''
#     /  \.-"""-./  \
#     \    -   -    /
#      |   o   o   |
#      \  .-'"'-.  /
#       '-\__Y__/-'
#          `---`'''
#     print(text)
#     return
# PrintBear()
#
#
# def PrintBat():
# # this function prints a bat ascii - art
#     text = r'''
#       /\                 /\
#      / \'._   (\_/)   _.'/ \
#     /_.''._'--('.')--'_.''._\
#     | \_ / `;=/ " \=;` \ _/ |
#      \/ `\__|`\___/`|__/`  \/
#              \(/|\)/       '''
#     print(text)
#     return
# PrintBat()


# def GiveWorkingDay():
# # prints the nearest working day date
#     from datetime import date
#     from datetime import timedelta
#     day = date.today()
#     # day = date(2019,3,25)
#     if day.weekday() == 5:
#         workingday = day + timedelta(days = 2)
#     elif day.weekday() == 6:
#         workingday = day + timedelta(days = 1)
#     else:
#         workingday = day
#     print("working day for", day, "is", workingday)
#     return
#
# GiveWorkingDay()




# import datetime
# def DayToLastDayThisYear():
#     #ile dni zostało do sylwestra
#     dateToday = datetime.date.today()
#     current_year = dateToday.year
#     date_end_year = datetime.date(current_year, 12, 31)
#     delta = date_end_year - dateToday
#     print(delta.days)
#     return
# DayToLastDayThisYear()





# def GiveWorkingDay(year, month, day):
# # prints the nearest working day date
#     from datetime import date
#     from datetime import timedelta
#     # day = date.today()
#     day = date(year, month, day)
#     if day.weekday() == 5:
#         workingday = day + timedelta(days = 2)
#     elif day.weekday() == 6:
#         workingday = day + timedelta(days = 1)
#     else:
#         workingday = day
#     print("working day for", day, "is", workingday)
#     return
#
# GiveWorkingDay(2019, 3, 26)
# GiveWorkingDay(2019, 3, 27)
# GiveWorkingDay(2019, 3, 28)
# GiveWorkingDay(2019, 3, 29)
# GiveWorkingDay(2019, 3, 30)
# GiveWorkingDay(day=6, month=12, year=2019)





# def PrintAnimal (animal):
#     if animal == "cat":
#         print( r'''
#        |\---/|
#        | o_o |
#         \_^_/''')
#     elif animal == "bear":
#         print(r'''
#     /  \.-"""-./  \
#     \    -   -    /
#      |   o   o   |
#      \  .-'"'-.  /
#       '-\__Y__/-'
#          `---`''')
#     elif animal == "bat":
#         print (r'''
#       /\                 /\
#      / \'._   (\_/)   _.'/ \
#     /_.''._'--('.')--'_.''._\
#     | \_ / `;=/ " \=;` \ _/ |
#      \/ `\__|`\___/`|__/`  \/
#              \(/|\)/       ''')
#     else:
#         print(" Nie ma takiego zwierzadka")
#     return
#
# PrintAnimal("bat")








# from datetime import date
# def DayToLastDayThisYear(year, month, day):
#     #ile dni zostało do sylwestra
#     dateToday = date(year, month, day)
#     date_end_year = date(year, 12, 31)
#     delta = date_end_year - dateToday
#     print(delta.days)
#     return
# DayToLastDayThisYear(2019, 4,2)





# def GiveWorkingDay(year, month = 1, day = 1):
# # prints the nearest working day date
#     from datetime import date
#     from datetime import timedelta
#     # day = date.today()
#     day = date(year, month, day)
#     if day.weekday() == 5:
#         workingday = day + timedelta(days = 2)
#     elif day.weekday() == 6:
#         workingday = day + timedelta(days = 1)
#     else:
#         workingday = day
#     print("working day for", day, "is", workingday)
#     return
#
# GiveWorkingDay(2019, 3)
# GiveWorkingDay(2019, 3, 19)
# GiveWorkingDay(2019)




# from datetime import date
# from datetime import timedelta
# def GiveWorkingDay(year = date.today().year, month = date.today().month, day = date.today().day):
# # prints the nearest working day date
#
#     day = date(year, month, day)
#     if day.weekday() == 5:
#         workingday = day + timedelta(days = 2)
#     elif day.weekday() == 6:
#         workingday = day + timedelta(days = 1)
#     else:
#         workingday = day
#     print("working day for", day, "is", workingday)
#     return
#
# GiveWorkingDay(2019, 3)
# GiveWorkingDay(2019, 3, 19)
# GiveWorkingDay(2019)




# def PrintAnimal (animal):
#     if animal == "cat":
#         print( r'''
#        |\---/|
#        | o_o |
#         \_^_/''')
#         print("PARAMETR ZOSTAL PODANY POPRAWNIE")
#     elif animal == "bear":
#         print(r'''
#     /  \.-"""-./  \
#     \    -   -    /
#      |   o   o   |
#      \  .-'"'-.  /
#       '-\__Y__/-'
#          `---`''')
#         print("PARAMETR ZOSTAL PODANY POPRAWNIE")
#     elif animal == "bat":
#         print (r'''
#       /\                 /\
#      / \'._   (\_/)   _.'/ \
#     /_.''._'--('.')--'_.''._\
#     | \_ / `;=/ " \=;` \ _/ |
#      \/ `\__|`\___/`|__/`  \/
#              \(/|\)/       ''')
#         print("PARAMETR ZOSTAL PODANY POPRAWNIE")
#     else:
#         print("PARAMETR NIE ZOSTAL PODANY POPRAWNIE")
#     return
#
# PrintAnimal("cat")






# from datetime import date
# def DayToLastDayThisYear(year = date.today().year, month = date.today().month, day = date.today().day):
#     #ile dni zostało do sylwestra
#     dateToday = date(year, month, day)
#     date_end_year = date(year, 12, 31)
#     delta = date_end_year - dateToday
#     print(delta.days)
#     return
# DayToLastDayThisYear()




# from datetime import date
# from datetime import timedelta
# def GiveWorkingDay(year = date.today().year, month = date.today().month, day = date.today().day):
# # prints the nearest working day date
#     day = date(year, month, day)
#     if day.weekday() == 5:
#         workingday = day + timedelta(days = 2)
#     elif day.weekday() == 6:
#         workingday = day + timedelta(days = 1)
#     else:
#         workingday = day
#     return workingday
# nextworkingday = GiveWorkingDay(2019, 3, 26)
# print("Next working day after", 2019, 3, 26, "is", nextworkingday)
# nextworkingday = GiveWorkingDay()
# print("Next working day after today is", nextworkingday)
# print("Next working day after today is ", GiveWorkingDay(2020, 5, 7))




# def PrintAnimal (animal):
#     if animal == "cat":
#         print( r'''
#        |\---/|
#        | o_o |
#         \_^_/''')
#         print("PARAMETR ZOSTAL PODANY POPRAWNIE")
#         return True
#     elif animal == "bear":
#         print(r'''
#     /  \.-"""-./  \
#     \    -   -    /
#      |   o   o   |
#      \  .-'"'-.  /
#       '-\__Y__/-'
#          `---`''')
#         print("PARAMETR ZOSTAL PODANY POPRAWNIE")
#         return True
#     elif animal == "bat":
#         print (r'''
#       /\                 /\
#      / \'._   (\_/)   _.'/ \
#     /_.''._'--('.')--'_.''._\
#     | \_ / `;=/ " \=;` \ _/ |
#      \/ `\__|`\___/`|__/`  \/
#              \(/|\)/       ''')
#         print("PARAMETR ZOSTAL PODANY POPRAWNIE")
#         return True
#     else:
#         print("PARAMETR NIE ZOSTAL PODANY POPRAWNIE")
#         return False
#
#
# printed = PrintAnimal("bat")
# print(printed)
#
#
#
# from datetime import date
# def DayToLastDayThisYear(year = date.today().year, month = date.today().month, day = date.today().day):
#     #ile dni zostało do sylwestra
#     dateToday = date(year, month, day)
#     date_end_year = date(year, 12, 31)
#     delta = date_end_year - dateToday
#     return delta.days
#
# liczbadni = DayToLastDayThisYear()
# print(liczbadni)







# def DoAction (action, parameter):
#     print("action:", action)
#     print("parameter:", parameter)
#     return
# DoAction("buy", "shoes")
#
#
#
#
# def DoAction (action, *parameter):
#     # gwiazdka oznacza, że to co przychodzi na to miejsce nie jest pojedynczym parametrem
#     print("action:", action)
#     print("parameter:", parameter)
#     for element in parameter:
#         print("element:", element)
#     return
# DoAction("buy", "shoes", "dres")

#
#
#
# def DoAction (action, what, **parameter):
#     # gwiazdka oznacza, że to co przychodzi na to miejsce nie jest pojedynczym parametrem, ktory stał sięsłownikiem
#     print("action:", action)
#     print("what: ", what)
#     print("parameter:", parameter)
#     for element in parameter:
#         print(element, "=", parameter[element])
#     return
# DoAction("buy", "shoes", size = 38, color = "red", type = "hight")
#
#
#
#
#
#
# def PrintAnimal (*animals):
#     cat = ( r'''
#        |\---/|
#        | o_o |
#         \_^_/''')
#
#     bear = (r'''
#     /  \.-"""-./  \
#     \    -   -    /
#      |   o   o   |
#      \  .-'"'-.  /
#       '-\__Y__/-'
#          `---`''')
#
#     bat =  (r'''
#       /\                 /\
#      / \'._   (\_/)   _.'/ \
#     /_.''._'--('.')--'_.''._\
#     | \_ / `;=/ " \=;` \ _/ |
#      \/ `\__|`\___/`|__/`  \/
#              \(/|\)/       ''')
#
#     inne = ("brak")
#     for animal in animals:
#         if animal == "cat":
#             print(cat)
#         elif animal == "bear":
#             print(bear)
#         elif animal == "bat":
#             print(bat)
#         else:
#             print(inne)
#     return
#
# PrintAnimal("cat", "bat", "waz")
#
#
#
#
# from datetime import date
# def DayToLastDayThisYear(*dane):
#     #ile dni zostało do sylwestra
#     for date_today in dane:
#         date_end_year = date(date_today.year, 12, 31)
#         delta = date_end_year - date_today
#         print("data:", date_today, "za pozostalo do konca roku", delta.days)
#     return
# DayToLastDayThisYear(date(2019, 3,26), date(2020, 8, 7))
#



# def WeakDayInFrance(dayNymber):
#     names = {0 : "lundi", 1 : "mardi", 2 : "marcredi", 3 : "jeudi", 4 : "vendredi", 5 : "samedi", 6 : "dimanche"}
#     return names.get(dayNymber, "error") # zwraca odpowiednią wartośc, ma wybrac z listy odpowiednią wartośc a gdyby jej nie bylo to error
#
# print(WeakDayInFrance(4))



# import math
# def GiveGeomSeqElement (a1 = 2, factor = 2, index = 2):
#     # oblicza wartosc ciagu geometrycznego
#     wzor = factor ** (index - 1) * a1
#     return wzor
#
# print(GiveGeomSeqElement(1, 2, 64))


# import math
# def GiveGeomSeqElement (a1 = 2, factor = 2, index = 2):
#     # oblicza wartosc ciagu geometrycznego
#     wzor = factor ** (index - 1) * a1
#     return wzor
# a1 = 3
# factor = 2
# maxindex = 10
# for i in range(1, maxindex):
#     print(GiveGeomSeqElement(a1, factor, i))



# def GiveFactorForGeomSeq (termin, nexttermin):
#     # wyznacza awrtosc wspolczynnika
#     wynik = nexttermin / termin
#     return wynik
# print(GiveFactorForGeomSeq(12, 24))




# def GiveSumOfNElementsGeomSeq (a1 = 2, factor = 2, n = 2):
#     # wyznacza sume pierwszych wyrazow ciagu
#     wzor = (a1 * (1 - factor **n)) / (1 - factor)
#     return wzor
# print(GiveSumOfNElementsGeomSeq(2, 3, 4))



# import geom # dolaczenie wlasnej biblioteki
# print(geom.GiveSumOfNElementsGeomSeq())



# filname = input("Enter lilname: ")
# print("The fil name is %s" % filname)


# filesize = input("Enter the max file size: ")
# print("The max size is: %d " % int(filesize))


# while True:
#     filesizeSTR = input("Enter the max file size (MB): ")
#     if filesizeSTR.isdecimal():
#         filesizeINT = int(filesizeSTR)
#         break
#
# print(" The max size in (MB) is: %d" % (filesizeINT * 1025))




# def check_int(s):
#     if s[0] in ('-', '+'):
#         return s[1:].isdigit()
#     return s.isdigit()
#
# while True:
#     a = input("a: ")
#     b = input("b: ")
#     c = input("c: ")
#     aI = int(a)
#     bI = int(b)
#     cI = int(c)
#     if not a.isdigit() and not b.isdigit() and not c.isdigit():
#         print("Zle dane")
#         break
#     elif aI == 0:
#         print("To nie jest rownanie kwadratowe")
#         break
#     else:
#         delta = bI ** 2 - 4 * aI * cI
#         if delta < 0:
#             print("Brak poprawnych rozwiazan")
#             break
#         elif delta == 0:
#             x1 = -bI / (2 * aI)
#             print("x1 = %d" % x1)
#             break
#         else:
#             x1 = (-bI - delta ** 0.5) / (2 * aI)
#             x2 = (-bI + delta ** 0.5) / (2 * aI)
#             print("x1 = %d, x2 = %d" % (x1, x2))
#             break



'''modół OS umozliwia  nam dostep do plików'''
''' funkcja  'os.getcwd' zwraca informacje o bierzącym katalogu'''
# import os
# import time
# print("Current dictionary is: ", os.getcwd())
# '''mój program chce w bierzacym katalogu zapisac plik i umiescic w nim np. rezultaty wykonywania pewnych obliczen '''
# currentDir = os.getcwd()
# filename = "results.txt" # wymyslona dowolna nazwa pliku
# fullpatch = os.path.join(currentDir, filename) # laczenie tak aby powstala sciezka do pliku ze sciezka do katalogu
# '''sa dwa rodzaje sciezek wzgledna(okresla sciezke pliku wzgledem polozonego katalogu) i bezwzgledna'''
# print(fullpatch)
# relativePath = "output.txt"
# print(os.path.abspath(relativePath)) # odpowiada nam jaka jest bezwzgledna scizka do pliku litera dysku, katalogi oraz nazwa tego pliku
# filepath = "/Users/justyna/test/hahah.kl"
# print(os.path.basename(filepath)) # zwraca tylko nazwę pliku
# print(os.path.dirname(filepath)) #zwraca sciezke dostępu do katalogu w ktorym ten plik sie znajduje
# print(os.path.exists(filepath)) # sprawdza czy plik lub folder istnieje
# '''jakie wlasciwosci z plikumozna wydobyc'''
# if os.path.exists(filepath):
#     print(os.path.getmtime(filepath)) # data utworzenia modyfikacji lub ostatniego otworzenia pliku
#     print(time.localtime(os.path.getmtime(filepath)))
#     print(os.path.getsize(filepath)) # rozmiar pliku zwracany w bajtach
#     print(os.path.isfile(filepath)) # czy sciezka identyfikuje plik
#     print(os.path.isdir(filepath))# - || - katalogu
#     print(os.path.split(filepath)) # oderwanie ostatniego fragmentu nazwy ze sciezki dostepu do pliku lub katalogu
#     print(os.path.split(filepath)[1]) # odwaolanie do pierwszej wartosci
#     print(os.path.splitdrive(filepath)) # oderwanie nazwy dysku oraz sciezka dostepu do pliku
#     print(os.path.splitdrive(filepath)[0]) # oderwanie tylko dysku



# import os
# import time
# dir = input("Podaj katalog: ")
# if os.path.exists(dir) and os.path.isdir(dir):
#     file = input("Nazwa pliku: ")
#     calosc = os.path.join(dir, file)
#     if os.path.exists(calosc) and os.path.isfile(calosc):
#         print(time.localtime(os.path.getmtime(calosc)))
#         print(os.path.getsize(calosc))
#         print(os.getcwd())
#         print(os.path.relpath(calosc))
#     else:
#         print("plik nie istnieje")
#
# else:
#     print("katalog nie istnieje")

# liczba = int(input("Podaj liczbę"))
# if liczba % 2 == 0:
#     print("%d jest liczbą parzystą " % (liczba))
# else:
#     print("%d jest liczbą nieparzystą " % (liczba))




# import os
# fileIsOk = False
# while not fileIsOk:
#     filname = input("Nazwa pliku: ")
#     if os.path.isfile(filname): # sprawdza czy taki plik istnieje:
#         fileIsOk = True
#     print(filname)




# import os
# while True:
#     filname = input("Nazwa pliku: ")
#     if os.path.isfile(filname): # sprawdza czy taki plik istnieje:
#         break
#     else:
#         print("Niepoprawna nazwa pliku, sprobuj ponownie")
#
#     print(filname)




# import os
# from datetime import date
# nazwa_katalogu_wejsciowego = "/temp/ćwiczenia/data_input"
# nazwa_katalogu_wyjsciowego = "/temp/ćwiczenia/yyyy-mm-dd"
# data = date(year=date.today().year, month=date.today().month, day=date.today().day)
# print(data)
# czy_nie_ma_katalogu = "/temp/ćwiczenia/%s" %(data)
# print(os.path.exists(nazwa_katalogu_wejsciowego))
# print(os.path.exists(nazwa_katalogu_wyjsciowego))
# print(os.path.exists(czy_nie_ma_katalogu))
# if os.path.exists(nazwa_katalogu_wejsciowego) and os.path.exists(nazwa_katalogu_wyjsciowego) and not os.path.exists(czy_nie_ma_katalogu):
#     print("wszystko dobrze")
# elif not os.path.exists(nazwa_katalogu_wejsciowego) and not os.path.exists(nazwa_katalogu_wyjsciowego):
#     print("brak katalogu wyjsciowego oraz wejsciowego")
# elif not os.path.exists(nazwa_katalogu_wejsciowego) and os.path.exists(nazwa_katalogu_wyjsciowego):
#     print("brak katalogu wejsciowego")
# elif os.path.exists(nazwa_katalogu_wejsciowego) and not os.path.exists(nazwa_katalogu_wyjsciowego):
#     print("brak katalogu wyjsciowego")
# else:
#     print("dwa katalogi z dzisiajsza data")
#     print("usun niepotrzebny")


# import os
# from datetime import date
# nazwa_katalogu_wejsciowego = "/temp/ćwiczenia/data_input"
# nazwa_katalogu_wyjsciowego = "/temp/ćwiczenia/data_output"
# data = date(year=date.today().year, month=date.today().month, day=date.today().day)
# katalog_dzienny = os.path.join(nazwa_katalogu_wyjsciowego, data.strftime("%Y-%m-%d"))
# istnienie_katalogu_wejsciowego = os.path.exists(nazwa_katalogu_wejsciowego) and os.path.isdir(nazwa_katalogu_wejsciowego)
# istnienie_katalogu_wyjsciowego = os.path.exists(nazwa_katalogu_wyjsciowego) and os.path.isdir(nazwa_katalogu_wyjsciowego)
# istnienie_katalogu_dziennego = os.path.exists(katalog_dzienny) and (os.path.isdir(katalog_dzienny) or os.path.isfile(katalog_dzienny))
# print(istnienie_katalogu_wejsciowego)
# print(istnienie_katalogu_wyjsciowego)
# print(istnienie_katalogu_dziennego)
# if istnienie_katalogu_wejsciowego and istnienie_katalogu_wyjsciowego and not istnienie_katalogu_dziennego:
#     print("wszystko dobrze")
# elif not istnienie_katalogu_wejsciowego and not istnienie_katalogu_wyjsciowego:
#     print("brak katalogu wyjsciowego oraz wejsciowego")
# elif not istnienie_katalogu_wejsciowego and istnienie_katalogu_wyjsciowego:
#     print("brak katalogu wejsciowego")
# elif istnienie_katalogu_wejsciowego and not istnienie_katalogu_wyjsciowego:
#     print("brak katalogu wyjsciowego")
# else:
#     print("dwa katalogi z dzisiajsza data")
#     print("usun niepotrzebny")






# '''WCZYTYWANIE PLIKÓW'''
# file = open("/temp/studia/download/waz2.txt", "r") # odczytanie pliku a literka "r" oznacza że tekst zostal otwarty tylko na odczyt
# content = file.read() # odczytanie pliku
# print(content)
# file.close()
#
# with open("/temp/studia/download/waz2.txt", "r") as file: # samo sie otwiera, robi coś i zamyka
#     content = file.read()
#     print(content)
#
# '''ta metoda jest dla małych plików, jeśli jest on duży należy zrobić to w sposób'''
# with open("/temp/studia/download/formularz.txt", "r") as file: # samo sie otwiera, robi coś i zamyka
#     for line in file:
#         print(line)

# '''wczytywanie fragmentu pliku'''
# with open("/temp/studia/download/formularz.txt", "r") as file:
#     fragment = file.read(20)
#     while fragment:
#         print(file.tell(), fragment) # file.tell() odpowiada za wyswietlenie, w ktorym momencie sie znajduje
#         fragment = file.read(20)
#
# with open("/temp/studia/download/formularz.txt", "r") as file:
#     fragment = file.read(20)
#     while fragment:
#         print(fragment)
#         fragment = file.read(20)

# with open("/temp/studia/download/formularz.txt", "r") as file:
#     content = file.readline()
#     print(content)





# '''wyswietlenie linijek tekstu'''
# with open("/temp/ćwiczenia/zamowienia.txt", "r") as zamowienia:
#     for line in zamowienia:
#         print(line)
# '''usuwanie ENTER'''
# with open("/temp/ćwiczenia/zamowienia.txt", "r") as zamowienia:
#     for line in zamowienia:
#         wyswietl = line[:line.find("\n")]
#         print(wyswietl)
# '''dzielenie linijki ze wzgledu na przecinki'''
# with open("/temp/ćwiczenia/zamowienia.txt", "r") as zamowienia:
#     for line in zamowienia:
#         wyswietl = line[:line.find("\n")]
#         order = wyswietl.split(",")
#         print(order)
# '''wyswietlanie komuikatu w zaleznosci od dlugosci order'''
# with open("/temp/ćwiczenia/zamowienia.txt", "r") as zamowienia:
#     for line in zamowienia:
#         wyswietl = line[:line.find("\n")]
#         order = wyswietl.split(",")
#         if len(order) == 3:
#             print('Order from drugstore "%s", item "%s", amount %s' % (order[0], order[1], order[2]))
#         else:
#             print("Line %s malformed!!!" % (line))
# print("koniec")





# '''PISANIE W PLIKACH'''
# filename = "/temp/ćwiczenia/pansrwa.txt"
# line = "Europe"
# cites = ["London", "Berlin", "Paris", "Warsaw", "Madrit", "Rome"]
# file = open(filename, "w") #otwieranie pliku do edytacji
# file.write(line + "\n") # pisanie w tym pliku
# file.write("\n") # dopiesanie nowej lini
# file.writelines(cites) # spoisywanie listy wartości
# file.close() # zamykanie pliku

# filename = "/temp/ćwiczenia/pansrwa.txt"
# line = "Europe"
# cites = ["London", "Berlin", "Paris", "Warsaw", "Madrit", "Rome"]
# file = open(filename, "w") #otwieranie pliku do edytacji
# file.write(line + "\n") # pisanie w tym pliku
# for miasto in cites:
#     file.write(miasto + "\n")
# file.close() # zamykanie pliku
#
# '''DOPISYWANIE DANYCH'''
# filename = "/temp/ćwiczenia/pansrwa.txt"
# line = "Europe"
# cites = ["London", "Berlin", "Paris", "Warsaw", "Madrit", "Rome"]
# file = open(filename, "a") #otwieranie pliku do edytacji
# file.write(line + "\n") # pisanie w tym pliku
# for miasto in cites:
#     file.write(miasto + "\n")
# file.close() # zamykanie pliku
#
# '''WCZYTYWANIE DANYCH ORAZ OTWIERA PLIK BY W NIM EDYTOWAC'''
# filename = "/temp/ćwiczenia/pansrwa.txt"
# line = "Europe"
# cites = ["London", "Berlin", "Paris", "Warsaw", "Madrit", "Rome"]
# file = open(filename, "w+") #otwieranie pliku do edytacji
# file.write(line + "\n") # pisanie w tym pliku
# for miasto in cites:
#     file.write(miasto + "\n")
# file.close() # zamykanie pliku
# '''WCZYTYWANIE DANYCH ORAZ OTWIERA PLIK BY W NIM EDYTOWAC NIE USUWAJĄC WCZESNIEJSZYCH DANYCH'''
# filename = "/temp/ćwiczenia/pansrwa.txt"
# line = "Europe"
# cites = ["London", "Berlin", "Paris", "Warsaw", "Madrit", "Rome"]
# file = open(filename, "w+") #otwieranie pliku do edytacji
# file.write(line + "\n") # pisanie w tym pliku
# for miasto in cites:
#     file.write(miasto + "\n")
# file.close() # zamykanie pliku






import os
# webaddresses = []
# line = input("adres strony: ")
# while len(line): # dopuki linia nie jest pusta
#     line = "www." + line
#     webaddresses.append(line)
#     line = input("adres strony: ")
#
# dirname = "/temp/ćwiczenia/"
# filename = input("nazwa pliku:")
# filepath = os.path.join(dirname, filename)
# print(filepath)
# file = open(filepath, "w")
# for mail in webaddresses:
#     file.write(mail + "\n")
# file.close()
#
# filname = input("sciezka do pliku: ")
# while True:
#     if os.path.isfile(filname) == False:
#         print("sciezka niepoprawna")
#         print("sproboj ponownie")
#         filname = input("sciezka do pliku: ")
#     else:
#         print("sciezka poprawna")
#         break
#
# odczyt = open(filname, "r")
# print("strony: ")
# for line in odczyt:
#     if line.count(".pl"):
#         print("aders polski: ", line)
#     else:
#         print("adres nie jest polski: ", line)
# odczyt.close()




# import os
# webaddresses = []
# line = input("adres strony: ")
# while len(line): # dopuki linia nie jest pusta
#     line = "www." + line
#     webaddresses.append(line)
#     line = input("adres strony: ")
#
# polskie = open("/temp/ćwiczenia/pl.txt", "w")
# for mail in webaddresses:
#     if mail.endswith("pl"):
#         polskie.write(mail + "\n")
# polskie.close()
#
# niepolskie = open("/temp/ćwiczenia/panstwa.txt", "w")
# for cos in webaddresses:
#     if not cos.endswith("pl"):
#         niepolskie.write(cos + "\n")
# niepolskie.close()



# '''Jeśli spodziewam się jakiegoś błędu to uniemożliwi wywalenie programu'''
# takesPerPerson = 0
# try:
#     tasks = 32
#     personsStr = input("How many persons are there in the team: ")
#     personsInt = int(personsStr)
#     takesPerPerson = tasks / personsInt
# except:
#     print("Something went wrong...")
#
# print("Every person should have around", takesPerPerson, "takes")
#
# '''import sys sprawdza jaki typ błedu powstanie'''
# import sys
# takesPerPerson = 0
# try:
#     tasks = 32
#     personsStr = input("How many persons are there in the team: ")
#     personsInt = int(personsStr)
#     takesPerPerson = tasks / personsInt
# except:
#     print("Something went wrong...", sys.exc_info()[0]) # wypisanie jaki to typ błedu
# print("Every person should have around", takesPerPerson, "takes")




# import sys
# file_path = r'/temp/ćwiczenia/orders.txt'
# with open(file_path, "r") as file:
#     for line in file:
#         line = line.replace('\n', '')
#         order = line.split(',')
#         try:
#             pharmacy_name = order[0]
#             item = order[1]
#             amount = int(order[2])
#             print("Order from drugstore %s, item %s, amount %d" %(pharmacy_name, item, amount))
#         except:
#             print("blad: ", sys.exc_info()[0], " w ", line)
# print("Processing finished")



# '''Jeśli wiadomo jakie wystąpią błędy to można napisac komunikat do kazdego z nich'''
# import sys
# takesPerPerson = 0
# try:
#     tasks = 32
#     personsStr = input("How many persons are there in the team: ")
#     personsInt = int(personsStr)
#     takesPerPerson = tasks / personsInt
# except ValueError:
#     print("Sorry you need to enter an integer number")
# except ZeroDivisionError:
#     print("Sorry - yoy need to enter value > 0")
# except:
#     print("Something went wrong...", sys.exc_info()[0]) # dobrze jest zostawić na wypadek wystąpienia innego błędu
# print("Every person should have around", takesPerPerson, "takes")
#
#
#
#
#
# '''Każdy w błędu może zostać użyty w komunikacie, który będę dalej budować oraz zapamiętuje informacje o błędzie w zmiennej e'''
# import sys
# takesPerPerson = 0
# try:
#     tasks = 32
#     personsStr = input("How many persons are there in the team: ")
#     personsInt = int(personsStr)
#     takesPerPerson = tasks / personsInt
# except ValueError as e:
#     print("Sorry you need to enter an integer number", e)
# except ZeroDivisionError as e:
#     print("Sorry - yoy need to enter value > 0", e)
# except:
#     print("Something went wrong...", sys.exc_info()[0]) # dobrze jest zostawić na wypadek wystąpienia innego błędu
# print("Every person should have around", takesPerPerson, "takes")






#
# import sys
# file_path = r'/temp/ćwiczenia/orders.txt'
# with open(file_path, "r") as file:
#     for line in file:
#         line = line.replace('\n', '')
#         order = line.split(',')
#         try:
#             pharmacy_name = order[0]
#             item = order[1]
#             amount = int(order[2])
#             print("Order from drugstore %s, item %s, amount %d" %(pharmacy_name, item, amount))
#         except ValueError as e:
#             print("Problem with conversion. Check whether the amount is correct. Line:", line,  e)
#         except IndexError as e:
#             print("Missing information. Check whether the line is build of at least 3 fields separated by comma. Line:", line,  e)
#         except:
#             print("blad: ", sys.exc_info()[0], " w ", line)
# print("Processing finished")



# '''W przypadku jeśli nie dojdzie do żadnego błędu można tutaj jeszcze skorzystać z funkcji ELSE, która tylko wtedy się wykona'''
# '''Natomiast funkcja FINALLY wykoa się nie ważne czy dojdzie do błędu czy też nie np. można w tym miejscu zamknąć otwarte pliki'''
# import sys
# takesPerPerson = 0
# try:
#     tasks = 32
#     personsStr = input("How many persons are there in the team: ")
#     personsInt = int(personsStr)
#     takesPerPerson = tasks / personsInt
# except ValueError as e:
#     print("Sorry you need to enter an integer number", e)
# except ZeroDivisionError as e:
#     print("Sorry - yoy need to enter value > 0", e)
# except:
#     print("Something went wrong...", sys.exc_info()[0]) # dobrze jest zostawić na wypadek wystąpienia innego błędu
# else:
#     print("Every person should have around", takesPerPerson, "takes")
# finally:
#     print("Script finished with/without errors")






# import os
# import sys
# line = input("Cena za kolejny kurs: ")
# sciezka = input("Scieżka do pliku: ")
#
# try:
#     value = int(line)
#     with open(sciezka, "w") as plik:
#         plik.write(line)
#         print("sciezka poprawna")
# except FileNotFoundError as e:
#     print("Error opening file", e)
# except ValueError as e:
#     print("The value entered cannot be converted to a number", e)
# except:
#     print("SORRY - WE HAVE AN ERROR", sys.exc_info()[0])
# else:
#     print("Actions completed successfully")
