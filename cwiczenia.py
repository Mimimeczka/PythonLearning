'''Dektoratory HTML'''
# def bold(function):
#     # pogrubienie
#     def wrapper(text):
#         func = function(text)
#         temp_bold = "<b>" + str(func) + "</b>"
#         return temp_bold
#
#     return wrapper
#
#
# def italic(function):
#     # pochylenie
#     def wrapper(text):
#         # func = function(text)
#         temp_italic = "<i>" + str(function(text)) + "</i>"
#         return temp_italic
#
#     return wrapper
#
#
# def underline(function):
#     # podkreslenie
#     def wrapper(text):
#         func = function(text)
#         temp_italic = "<u>" + str(func) + "</u>"
#         return temp_italic
#
#     return wrapper
#
#
# @underline
# @bold
# @italic
# def say_hi(text):
#     return text
#
#
# print(say_hi("dupa"))

'''Dektorator log'''
# import time
#
#
# def log(function):
#     def wrapper(*param):
#         print("Nazwa funkcji:", function)
#         print("Argument(y):", param)
#         start_time = time.time()
#         result = function(param)
#         end_tme = time.time()
#         print("Czas wykonania:", str(end_tme - start_time))
#         return result
#     return wrapper
#
#
# @log
# def do_sth(*param):
#     return param
#
#
# print(do_sth("dupa", "dupa2"))

'''Klasa Product'''

#
# class Product:
#
#     def __init__(self, prod_id: int, name: str, price: float):
#         self.prod_id = prod_id
#         self.name = name
#         self.price = price
#
#     def print_product_info(self):
#         return "Produkt: " + self.name + ", id: " + str(self.prod_id) + ", cena: " + str(self.price) + " PLN"
#
#
# prod = Product(1, "Woda", 10.99)
# print(prod.print_product_info())


'''Klasa rejestrujaca czas pracy'''
# class Employee:
#
#     def __init__(self, name, last_name, pay_per_hour):
#         self.name = name
#         self.last_name = last_name
#         self.pay_per_hour = pay_per_hour
#         self.salary = 0.0
#
#     def register_time(self, hours):
#         if hours > 0:
#             if hours > 8:
#                 overtime = hours - 8
#                 self.salary += (overtime * (self.pay_per_hour * 2)) + (8 * self.pay_per_hour)
#
#             else:
#                 self.salary += hours * self.pay_per_hour
#
#     def pay_salary(self):
#         temp = self.salary
#         self.salary = 0.0
#         return temp
#
#
# empl = Employee("Justyna", "Zaczyk", 100.0)
# empl.register_time(5)
# print(empl.pay_salary())
# print(empl.pay_salary())
# empl.register_time(10)
# empl.register_time(10)
# print(empl.pay_salary())
# empl.pay_salary()
# print(empl.pay_salary())

'''zadanie 3'''

# class ElectrlCar:
#     def __init__(self, max_range):
#         self.max_range = max_range
#         self.to_charge = max_range
#
#     def car_drive(self, distance):
#         if self.max_range - distance > 0:
#             self.max_range -= distance
#         return "Pozostalo" + str(self.max_range)
#
#     def car_charge(self):
#         self.max_range = self.to_charge

'''zadanie 4'''
# class Product:
#     def __init__(self, prod_id: int, name: str, price: float):
#         self.prod_id = prod_id
#         self.name = name
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
# class Basket:
#     def __init__(self):
#         self.products = {}
#
#     def add_product(self, product, quantity):
#         self.products[product] = quantity
#
#     def count_total_price(self):
#         suma = 0
#         for x in self.products:
#             y = self.products[x]
#             suma += x.get_price() * y
#         return suma
#
#     def generate_report(self):
#         print("Produkty w koszyku")
#         for a in self.products:
#             print(f"{a.name} ({a.prod_id}), cena: {a.price}, ilosc: {self.products[a]}")
#         print("Suma:")
#         return self.count_total_price()
#
#
# produktA = Product(1, "Woda", 10.99)
# produktB = Product(2, "Chleb", 4.5)
# basked = Basket()
# basked.add_product(produktA, 5)
# basked.add_product(produktB, 5)
# print(basked.generate_report())


'''zadnie 5'''
# class CashMachine:
#     def __init__(self):
#         self.__money = []
#
#     def put_money(self, *put):
#         for x in sorted(put, reverse=True):
#             if x > 0:
#                 self.__money.append(x)
#
#     def is_available(self):
#         if len(self.__money) > 0:
#             return True
#         return False
#
#     def withdraw_money(self, money):
#         cash = []
#         for x in self.__money:
#             if x <= money:
#                 cash.append(x)
#                 money -= x
#
#         for y in cash:
#             self.__money.remove(y)
#
#         return cash
#
#
# cash_machine = CashMachine()
# print(cash_machine.is_available())
# cash_machine.put_money(200, 100, 50, 100)
# print(cash_machine.is_available())
# print(cash_machine.withdraw_money(450))
# print(cash_machine.is_available())


'''zadanie 6'''
# import math
# class Vector:
#     def __init__(self, vector_a, vector_b):
#         self.vector_a = vector_a
#         self.vector_b = vector_b
#
#     def __add__(self, other):
#         x = (self.vector_a + other.vector_a)
#         y = (self.vector_b + other.vector_b)
#         return Vector(x, y)
#
#     def __sub__(self, other):
#         x = (self.vector_a - other.vector_a)
#         y = (self.vector_b - other.vector_b)
#         return Vector(x, y)
#
#     def __mul__(self, other):
#         # dwa wektory nie mozna pomnożyć przez siebie tylko przez liczbe
#         x = (self.vector_a * other)
#         y = (self.vector_b * other)
#         return Vector(x, y)
#
#     def __eq__(self, other):
#         a = math.sqrt(self.vector_a + self.vector_b)
#         b = math.sqrt(other.vector_a + other.vector_b)
#         return a == b
#
#     def __str__(self):
#         return f"wektor posiada wspolrzedne x = {self.vector_a}, y = {self.vector_b}"
#
#
# wektorA = Vector(3, 4)
# wektorB = Vector(3, 4)
# wektorC = wektorA + wektorB
# print(wektorC * 2)
# print(wektorA == wektorC)


'''zadanie 7'''
# class Employee:
#     def __init__(self, name, last_name, pay_per_hour):
#         self.name = name
#         self.last_name = last_name
#         self.pay_per_hour = pay_per_hour
#         self.salary = 0.0
#
#     def register_time(self, hours):
#         if hours > 0:
#             if hours > 8:
#                 overtime = hours - 8
#                 self.salary += (overtime * (self.pay_per_hour * 2)) + (8 * self.pay_per_hour)
#
#             else:
#                 self.salary += hours * self.pay_per_hour
#
#     def pay_salary(self):
#         temp = self.salary
#         self.salary = 0.0
#         return temp
#
# class PremiumEmployee(Employee):
#     def give_bonus(self, bonus):
#         if bonus > 0:
#             self.salary += bonus
#
#
# employee = PremiumEmployee("Jaroslaw", "Slaby", 50.0)
# employee.register_time(8)
# employee.give_bonus(1000.0)
# print(employee.pay_salary())


'''zadanie 8'''
# class CashMachine:
#     def __init__(self, limit):
#         self.__money = []
#         self.limit = limit
#
#     def put_money(self, put):
#         if len(self.__money) + len(put) > self.limit:
#             raise NumberException("Brak miejsca")
#
#         for z in put:
#             if z % 10 != 0:
#                 raise NumberException("Zły banknot")
#
#         for x in sorted(put, reverse=True):
#             if x > 0:
#                 self.__money.append(x)
#
#     def is_available(self):
#         if len(self.__money) > 0:
#             return True
#         return False
#
#     def withdraw_money(self, money):
#         if sum(self.__money) < money:
#             raise NumberException("Brak banknotów")
#
#         cash = []
#         for x in self.__money:
#             if x <= money:
#                 cash.append(x)
#                 money -= x
#
#         for y in cash:
#             self.__money.remove(y)
#
#         return cash
#
#
# class NumberException(Exception):
#     # tworzennie nowego wyjątku
#     pass
#
#
#
# cash_machine = CashMachine(2)
# while True:
#
#     command = input("1 - wplata \n2 - wyplata\n0 - wyjscie ")
#     try:
#         x = int(command)
#
#         if x == 1:
#             cash = [int(x) for x in input("Banknoty do wplaty: ").split(" ")]
#             cash_machine.put_money(cash)
#             print("Wplacono:", sum(cash))
#
#         elif x == 2:
#             cash = int(input("Kwota do wypłaty: "))
#             print(cash_machine.withdraw_money(cash))
#
#         else:
#             print("Zakonczono")
#             break
#
#     except NumberException as e:
#         print(e)
#
#     except ValueError:
#         print("Wybrano zla wartosc")


'''zadanie 9'''
# class Product:
#     def __init__(self, prod_id: int, name: str, price: float):
#         self.prod_id = prod_id
#         self.name = name
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
# class Basket:
#     def __init__(self):
#         self.products = {}
#
#     @staticmethod
#     def with_products(products):
#         temp_basket = Basket()
#         for x in products:
#             temp_basket.add_product(x, quantity=1)
#         return temp_basket
#
#     def add_product(self, product, quantity):
#         self.products[product] = quantity
#
#     def count_total_price(self):
#         suma = 0
#         for x in self.products:
#             y = self.products[x]
#             suma += x.get_price() * y
#         return suma
#
#     def generate_report(self):
#         print("Produkty w koszyku")
#         for a in self.products:
#             print(f"{a.name} ({a.prod_id}), cena: {a.price}, ilosc: {self.products[a]}")
#         print("Suma:")
#         return self.count_total_price()
#
#
# produktA = Product(1, "Woda", 10.99)
# produktB = Product(2, "Chleb", 4.5)
# basked = Basket.with_products([produktA, produktB])
# print(basked.generate_report())

'''zadanie 10'''
# class Product:
#     prod_id = 0
#
#     @classmethod
#     def __init__(cls, name: str, price: float):
#         cls.name = name
#         cls.price = price
#         cls.prod_id += 1
#
#     def get_price(self):
#         return self.price
#
# produktA = Product("Woda", 10.99)
# print(produktA.prod_id)
# produktB = Product("Chleb", 4.5)
# print(produktB.prod_id)

'''zadanie 11'''
# class Element:
#     def __init__(self, value):
#         self.value = value
#
#     def render(self):
#         return self.value
#
#
# class HeaderElement(Element):
#     def __init__(self, value):
#         Element.__init__(self, value)
#
#     def render(self):
#         return Element.render(self) + "\n====="
#
#
# class LinkElement(Element):
#     def __init__(self, value, value_y):
#         Element.__init__(self, value)
#         self.value_y = value_y
#
#     def render(self):
#         return f"({Element.render(self)}) [http://{self.value_y}]"
#
#
# class Document:
#     def __init__(self):
#         self.elements = []
#
#     def add_element(self, element):
#         self.elements.append(element)
#
#     def render_document(self):
#         string = ""
#         for x in self.elements:
#             string += x.render()
#             string += "\n"
#         return string
#
#
# document = Document()
# document.add_element(HeaderElement("Header"))
# document.add_element(LinkElement("ABC", "abc.com"))
# document.add_element(Element("simple"))
# print(document.render_document())


'''zadanie 12'''
# class Product:
#     def __init__(self, prod_id: int, name: str, price: float):
#         self.prod_id = prod_id
#         self.name = name
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
# class Basket:
#     def __init__(self):
#         self.products = {}
#         self.value_discounts = []
#         self.percent_discounts = []
#
#     def add_discount(self, discount): # dodaj znizke kwotowa
#         self.value_discounts.append(discount)
#
#     def add_percent_discount(self, percent_discount): #dodaj znizke procentowa
#         self.percent_discounts.append((100 - percent_discount.get_discount()) / 100)
#
#     def add_product(self, product, quantity):
#         self.products[product] = quantity
#
#     def count_total_price(self):
#         suma = 0
#         for x in self.products:
#             y = self.products[x]
#             suma += x.get_price() * y
#
#         sum_discounts = 0
#         for z in self.value_discounts:
#             sum_discounts += z.get_discount()
#
#         percent_discount_value = 1.0
#         for percent in self.percent_discounts:
#             percent_discount_value *= percent
#
#         to_pay = (suma - sum_discounts) * percent_discount_value
#
#         if to_pay > 0:
#             return to_pay
#         return 0
#
#     def generate_report(self):
#         print("Produkty w koszyku")
#         for a in self.products:
#             print(f"{a.name} ({a.prod_id}), cena: {a.price}, ilosc: {self.products[a]}")
#         print("Suma:")
#         return self.count_total_price()
#
#
# class ValueDiscount:
#     def __init__(self, discount: float):
#         self.discount = discount
#
#     def get_discount(self):
#         return self.discount
#
#
# class PercentDiscount:
#     def __init__(self, discount: float):
#         self.discount = discount
#
#     def get_discount(self):
#         return self.discount
#
#
# produktA = Product(1, "Woda", 10.0)
# produktB = Product(2, "Chleb", 5.0)
# basked = Basket()
# basked.add_product(produktA, 6)
# basked.add_product(produktB, 10)
# # discount = ValueDiscount(3.0)
# # discountx = ValueDiscount(7.0)
# # basked.add_discount(discount)
# # basked.add_discount(discountx)
# # basked.add_percent_discount(PercentDiscount(20))
# # basked.add_percent_discount(PercentDiscount(30))
# print(basked.generate_report())

'''IERATORY I GENERATORY'''

# '''zadanie 1'''
# class Counter:
#     def __init__(self, number):
#         self.number = number
#         self.start = 0
#
#     def __iter__(self):
#         # iter zwraca iterator, cała klasa jest iteratorem
#         # bez tej metody nie da się napisać for
#         return self
#
#     def __next__(self):
#         # next z iteratorem idzie w parze
#         # ta metoda bedzie wykonana do momentu, w ktorym wejdzie w else
#         # raise StopIteration() - zakonczenie iterowania
#         num = self.start
#         self.start += 1
#         if num <= self.number:
#             return num
#         else:
#             raise StopIteration()
#
#
# for x in Counter(10):
#     print(x)

'''zadanie 2'''
# class Vowels:
#     def __init__(self, text):
#         self.text = text
#         self.number = 0
#
#     def __iter__(self):
#         # iter zwraca iterator, cała klasa jest iteratorem
#         # bez tej metody nie da się napisać for
#         return self
#
#     def __next__(self):
#         # next z iteratorem idzie w parze
#         # ta metoda bedzie wykonana do momentu, w ktorym wejdzie w else
#         # raise StopIteration() - zakonczenie iterowania
#         letter = self.text[self.number]
#         self.number += 1
#         if self.number < len(self.text):
#             if letter in "aeiouy":
#                 return letter
#             else:
#                 return ""
#         else:
#             raise StopIteration()
#
#
# for x in Vowels('ala ma kota a kott ma ale'):
#     print(x)

'''zadanie 3'''
'''Genetrator to taka funkcja która za każdym razem gdy coś chce wygenerować czyli stworzyć coś nowego
używa słowa kluczowego yield.'''
# class Vowels:
#     def __init__(self, text):
#         self.text = text
#
#     def get_vowels(self):
#         for letter in self.text:
#             if letter in "aeouiy":
#                 yield letter
#
#
# tekst = Vowels("ala ma kota a kot ma ale")
# for vovel in tekst.get_vowels():
#     print(vovel)

# def get_vowels(text):
#     for letter in text:
#         if letter in "aeouiy":
#             yield letter
# for x in get_vowels("ala ma kota a kot ma ale"):
#     print(x)

'''zadanie 4'''
# def tournament(players):
#     for x in players:
#         for y in players:
#             if x != y:
#                 yield x, y
#
# for p_a, p_b in tournament("abc"):
#     print(p_a, p_b)

'''obsługa plików'''
'''zadanie 1'''
# with open("/Users/justyna/Desktop/przepisy/risotto.txt", "r") as file:
#     number_line = 1
#     for line in file:
#         print(number_line, line)
#         number_line += 1

'''zadanie 3'''
# with open("/Users/justyna/Desktop/adresy.txt", "r") as file:
#     email = set()
#     for line in file:
#         if line.count("@") == 1 and line.count(".") >= 1 and line.count(" ") == 0:
#             email.add(line.lower())
#
#
# new_email = list(email)
# new_email.sort()
# with open("/Users/justyna/Desktop/nowe_adresy.txt", "w") as file:
#     for mail in new_email:
#         file.write(mail)

'''zadanie 4'''
# import os
# # os.listdir("/Users") # zwraca tablice z nazwami wszystkich plików i katalogów w danym katalogu
# def print_directory_content(path, level):
#     current_dir = os.listdir(path)
#     for file in current_dir:
#         if os.path.isdir(path + "/" + file):
#             print("|" + " " * (level * 4) + "-- " + path + "/" + file)
#             print_directory_content(path + "/" + file, level + 1)
#         else:
#             if current_dir.index(file) == (len(current_dir) - 1):
#                 print("|" + " " * (level * 4) + "\\-- " + file)
#             else:
#                 print("|" + " " * (level * 4) + "|-- " + file)
#
# print("test")
# print_directory_content(".", 0)

'''Biblioteka standardowa to taka gdzie nie musze nic dodatkowego importować'''
'''zadanie 1'''
# import json
# while True:
#     command = int(input("Wybierz opcje:\n1 - dodaj pracownika\n2 - wypisz procowników\n3 - usuń pracownika\n4 - wyjście\n"))
#     if command == 1:
#         file = open("/Users/justyna/Desktop/pracownicy.db", "a+")
#         name = input("Podaj imie: ")
#         last_name = input("Podaj nazwisko: ")
#         year = input("Podaj rok urodenia: ")
#         salary = input("Wynagrodzenie: ")
#         persons = {"Name": name, "Last name": last_name, "year of birth": year, "Salary": salary}
#         file.write(json.dumps(persons)) # konwertuje obiekt na str z jsonem i zapisuje go do pliku
#         file.write("\n")
#         file.close()
#     elif command == 2:
#         file = open("/Users/justyna/Desktop/pracownicy.db", "r")
#         number = 1
#         for line in file:
#             y = json.loads(line) # zwraca mape
#             print(number, "Imie %s, nazwisko %s, data urodzenia %s, wynagrodzenie %s." %(y["Name"], y["Last name"], y["year of birth"], y["Salary"]))
#             number += 1
#         file.close()
#     elif command == 3:
#         name_to_delete = input("Podaj numer pracownika do usunięcia: ")
#         with open("/Users/justyna/Desktop/pracownicy.db", "r") as file:
#             employees = []
#             for line in file:
#                 employees.append(line)
#         with open("/Users/justyna/Desktop/pracownicy.db", "w") as file:
#             for x in employees:
#                 if x.count(name_to_delete) == 0 :
#                     file.write(x)
#     else:
#         print("wyjscie")
#         break
# '''zadanie 2'''
# import json
# import urllib.request
#
# location = input("Podaj miasto: ")
# #urlib to biblioteka sluzaca do wykonywania zapytan http do zewnetrznych serwerow (cos jak przegladarka)
# location_response = urllib.request.urlopen("https://www.metaweather.com/api/location/search/?query=" + location).read().decode("utf-8")
# location_response_map = json.loads(location_response[1: len(location_response) - 1])
# woeid = location_response_map["woeid"]
#
# weather_response = urllib.request.urlopen("https://www.metaweather.com/api/location/" + str(woeid)).read().decode("utf-8")
# weather_response_map = json.loads(weather_response)
# print("Dzis:", weather_response_map["consolidated_weather"][0]["weather_state_name"])
# print("Jutro:", weather_response_map["consolidated_weather"][1]["weather_state_name"])

'''zadanie 3'''
# import tkinter
# from tkinter import ttk
# window = tkinter.Tk()
# info_dystans = tkinter.Label(window, text="Dystans")
# info_dystans.pack()
# dystans = tkinter.Entry(window, width=10)
# dystans.pack()
# info_spalanie = tkinter.Label(window, text="Spalanie")
# info_spalanie.pack()
# spalanie = tkinter.Entry(window, width=10)
# spalanie.pack()
# info_cena_paliwa = tkinter.Label(window, text="Cena paliwa")
# info_cena_paliwa.pack()
# cena_paliwa = tkinter.Entry(window, width=10)
# cena_paliwa.pack()
#
# def oblicz_koszt():
#     dystans_wartosc = float(dystans.get())
#     spalanie_wartosc = float(spalanie.get())
#     cena_wartosc = float(cena_paliwa.get())
#     koszt_wartosc = dystans_wartosc / 100 * spalanie_wartosc * cena_wartosc
#     koszt["text"] = str(koszt_wartosc)
#
# oblicz = ttk.Button(window, text="oblicz koszt", command=oblicz_koszt)
# oblicz.pack()
# info_koszt = tkinter.Label(window, text="Koszt przejazdu")
# info_koszt.pack()
# koszt = tkinter.Label(window, text="")`
# koszt.pack()
#
# window.mainloop()

'''zadanie 5'''
# import re
#
# zips = 0
# emails = 0
# dates = 0
#
# zip_regexp = "[0-9]{2}-[0-9]{3}"
# mail_regexp = "[a-zA-Z0-9\\.]+@{1}[a-zA-Z0-9]+.{1}[a-zA-z]{2,3}"
# date_regexp = "(0[1-9]|[12][0-9]|3[01]) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([0-9]{4})"
#
#
# with open("zips.txt") as file:
#     for line in file:
#         if re.match(zip_regexp, line): #match zwraca true jesli element pasuje do wzorca, w przeciwnym razie false
#             zips += 1
#         if re.match(mail_regexp, line):
#             emails += 1
#         if re.match(date_regexp, line):
#             dates += 1
#
#
# print(zips)
# print(emails)
# print(dates)
#
#
#
# import re
#
# zip_regexp = "[0-9]{2}-[0-9]{3}"
# mail_regexp = "[a-zA-Z0-9\\.]+@{1}[a-zA-Z0-9]+.{1}[a-zA-z]{2,3}"
# date_regexp = "(0[1-9]|[12][0-9]|3[01]) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([0-9]{4})"
#
# with open("zips.txt") as input_file:
#     content = input_file.read()
#     zips = re.findall(zip_regexp, content) #finall tworzy liste elementow pasujacych do wzorca
#     mails = re.findall(mail_regexp, content)
#     dates = re.findall(date_regexp, content)
#
# print(len(zips), zips)
# print(len(mails), mails)
# print(len(dates), dates)
#
#
#
#
'''zadanie 6'''
# import urllib.request #wykonanie jednowatkowe ok 33 sekundy
# import time
#
# start = time.time()
# for i in range(100): #jeden watek odpytuje api 100 razy
#     urllib.request.urlopen("https://www.metaweather.com/api/location/search/?query=Warsaw")
#
# end = time.time()
#
# print("Czas trwania: ", str(end - start))
#
#
# import _thread as thread #wielowatkowo przy uzyciu biblioteki thread - 0.0017 sek
# import urllib.request
# import time
#
#
# def call_api():
#     urllib.request.urlopen("https://www.metaweather.com/api/location/search/?query=Warsaw")
#
#
# start = time.time()
# for i in range(100):
#     thread.start_new_thread(call_api, ()) #startuje nowy watek i przekazuje funkcje do wykonania
#
# end = time.time()
#
# print("Czas trwania: ", str(end - start))
#
# import threading  #wielowatkowo przy uzyciu biblioteki threading i stworzeniu wlasnej klasy watku - ok 2 sek
# import urllib.request
# import time
#
#
# class ApiCall(threading.Thread):
#     def __init__(self):
#         super().__init__()
#
#     def run(self): #metoda run zawiera to, co watek ma zrobic
#         self.call_api()
#
#     def call_api(self):
#         urllib.request.urlopen("https://www.metaweather.com/api/location/search/?query=Warsaw")
#
#
# start = time.time()
#
# for i in range(100):
#     thread = ApiCall()
#     thread.start() #uruchomienie watku
#
# end = time.time()
#
# print("Czas trwania: ", str(end - start))


'''obliczenia numeryczne'''
'''zadanie 1'''
import numpy


powers = numpy.empty([10, 10], dtype=int)
num = 1
for i in range(0, 10):
    for j in range(0, 10):
        powers[i][j] = num * num
        num += 1
print(powers)
print()

zeros_ones = numpy.zeros([5, 5], dtype=int)
num = 1
for i in range(0, 5):
    for j in range(0, 5):
        if i != 0 and j != 0 and i != 4 and j != 4:
            zeros_ones[i, j] = num
print(zeros_ones)
print()

tabl_mnozenia = numpy.fromfunction(lambda x, y: x * y, (10, 10), dtype=int)
print(tabl_mnozenia)
