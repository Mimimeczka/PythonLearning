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







# class Dzialanie:
#     def __init__(self, number):
#         self.number = number
#
#     def __call__(self, razy):
#         return self.number * razy
#
# liczba = Dzialanie(5)
# print(liczba(3))




# class Foo:
#     # parameter = 1
#
#     def __init__(self):
#         self.__b = 3
#
#     @property
#     def b(self):
#         return self.__b
#
#     @b.setter
#     def b(self, valuse):
#         if valuse < 0:
#             self.__b = abs(valuse)
#         else:
#             self.__b = valuse
#
#
# liczba = Foo()
# liczba.b = -5
# print(liczba.b)




'''setery, getery, propercje'''
# class Foo:
#     # parameter = 1
#
#     def __init__(self):
#         self.__c = 3
#
#     def gets_c(self):
#         return self.__c
#
#     def set_c(self, valuse):
#         self.__c = abs(valuse)
#
#         # if valuse < 0:
#         #     self.__a = abs(valuse)
#         # else:
#         #     self.__a = valuse
#
#     c = property(gets_c, set_c)
#
#
# liczba = Foo()
# liczba.c = -5
# # liczba.set_c(-11)

# print(liczba.gets_c())
# print(liczba.c)
# print(liczba.__a) # nie zadziała




'''hermetyzzacja'''
# class Temp:
#     def __init__(self):
#         self.a = 3
#         self.__a = 5
#
#     def wyswietl (self):
#         print(self.a)
#         print(self.__a)


# objekt = Temp()
# objekt.wyswietl()






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
#     @staticmethod
#     def Klakson():
#         print("pippp")
#
#
# samochod = Car("skoda")
# samochodd = Car("skoda")
# print(samochod.HowManyCar)
# print(Car.HowManyCar)
# samochod.AddCar()
# print(samochod.HowManyCar)
# print(Car.HowManyCar)
# samochod.Klakson()
# samochod.HowManyCar()


# '''INACZEJ'''

class Car:
    SumCar = 0
    @classmethod
    def __init__(cls, self, brand):
        self.brand = brand
        cls.SumCar += 1


class A:
    pass

a = A()

samochod = Car(a, "fiat")
samochod2 = Car(a, "srat")
samochod3 = Car(Car, "dupa")

print(a.brand)


a.qwert = 8


















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





'''POLOMORFIZM - wbudowany w język
Mechanizm pozwalający na operowanie w różnych grupach w ten sam sposób np. przykład kaczki
Można osiągnąć przy pomocy dziedziczenia lub też nie przykład Robot'''
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
#
# kotek = Cat("12", "Mruczek", "Pers")
# kotek.printInformation()


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



'''EQ, STR, REPR'''
# class Obiekt:
#     def __init__(self, kolor, material):
#         self.kolor = kolor
#         self.material = material
#
#     def __eq__(self, other):
#         return self.kolor == other.kolor and self.material == other.material
#
#     # def __str__(self):
#     #     return f"Mam kolor {self.kolor}, jestem z materiału {self.material}"
#
#     def __repr__(self):
#         tekst = repr(Obiekt)
#         return f"Naleze do klasy {tekst}. Mam kolor {self.kolor}, jestem z materiału {self.material}"
#
#
# testA = Obiekt("czerwony", "bawelna")
# testB = Obiekt("czerwony", "bawelna")
# print(testA == testB)
# print(testA)




'''OPERATORY PRZECIĄŻANIA'''

# class Clock:
#     def __init__(self, hour=0, minutes=0, seconds=0):
#         self.hour = hour
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def editTime(self, hour=0, minutes=0, seconds=0):
#         if self.seconds + seconds >= 60:
#             self.minutes += (self.seconds + seconds) // 60
#             self.seconds = (self.seconds + seconds) % 60
#         else:
#             self.seconds += seconds
#
#         if self.minutes + minutes >= 60:
#             self.hour += (self.minutes + minutes) // 60
#             self.minutes = (self.minutes + minutes) % 60
#         else:
#             self.minutes += minutes
#
#         if self.hour + hour >= 24:
#             if self.hour + hour == 24:
#                 self.hour = 0
#             elif self.hour + hour > 24:
#                 self.hour = (self.hour + hour) % 24
#             else:
#                 self.hour += hour
#
#     def __str__(self):
#         return f"Czas to {self.hour}:{self.minutes}:{self.seconds}"
#
#     def __eq__(self, other):
#         return self.hour == other.hour and self.minutes == other.minutes and self.seconds == other.seconds
#
#     def __add__(self, other):
#         zegarek = Clock(self.hour, self.minutes, self.seconds)
#         zegarek.editTime(other.hour, other.minutes, other.seconds)
#         return zegarek
#
#
# zegarek = Clock(5, 45, 12)
# zegarekA = Clock(5, 45, 12)
# zegarek.editTime(18, 20, 10)
# print(zegarek)
# zegarekB = zegarek + zegarekA
# print(zegarekB)
#
# clock_one = Clock(23, 0, 0)
# clock_two = Clock(3, 0, 0)
#
# print("hours counting test")
# print(clock_one + clock_two)
# print(clock_two == clock_one)
#
'''ZAPISYWANIE OBIEKTU DO PLIKU'''
#
# import _pickle as pick
# file = open("//temp/ćwiczenia/pl.txt", "wb")
# pick.dump(zegarek, file)
# file.close()
#
# print("ODCZYT")
# filr_pick = open("/temp/ćwiczenia/pl.txt", "rb")
# zegarek = pick.load(filr_pick)
# filr_pick.close()
# print(zegarek)




#
#
# def suma(*a):
#     wynik = 0
#     for c in a:
#         wynik += cm
#     return wynik
#
# lista = [1, 2, 3, 4]
# print(suma(*lista))





# class Book:
#     def __init__(self, author, title, pages):
#         self.author = author
#         self.title = title
#         self.pages = pages
#
#     def __str__(self):
#         return f"Ksiazka {self.author} pod tytułem {self.title} zawiera {self.pages} stron"
#
#     def __eq__(self, other):
#         return self.author == other.author and self.title == other.title
#
#     def __radd__(self, other):
#         if isinstance(other, Book):
#             return self.pages + other.pages
#         else:
#             return self.pages + other
#
#     def __lt__(self, other):
#         if self.pages < other.pages:
#             return True
#         return False
#
#
# ksiazkaA = Book("Marek", "cos gdzies", 15)
# ksiazkaB = Book("Marek", "cos gdzies", 175)
# ksiazkaC = Book("Waldek", "cos ktos", 235)
#
# zbior = [ksiazkaA, ksiazkaB, ksiazkaC]
# suma_stron = sum(zbior)
# print(suma_stron)
#
# if ksiazkaA > ksiazkaB:
#     print("Książka A jest dluzsza")
# else:
#     print("Książk B jest głuższa")
