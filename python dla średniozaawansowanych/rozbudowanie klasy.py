'''wywołanie instancji klasy'''
# class Zakupy:
#
#     def __init__(self, lista):
#         self.lista = lista
#
#     def __call__(self, obiekt):
#         self.lista.append(obiekt)
#
# lista_zakupow = Zakupy([])
# print(lista_zakupow.lista)
#
# lista_zakupow.lista.append("pietruszka")
# print(lista_zakupow.lista)
#
# lista_zakupow("marchewka")
# print(lista_zakupow.lista)
#
# class  NoDuplicates:
#
#     def __init__(self, list):
#         self.list = list
#
#     def __call__(self, *new_items):
#         for x in new_items:
#             if not x in self.list:
#                 self.list.append(x)
#
#
# my_no_dup_list = NoDuplicates([])
# print(my_no_dup_list.list)
#
# my_no_dup_list('keyboard', 'mouse')
# print(my_no_dup_list.list)
#
# my_no_dup_list('keyboard', 'mouse', 'pendrive')
# print(my_no_dup_list.list)
#
# my_no_dup_list('charger','pendrive')
# print(my_no_dup_list.list)


'''klasa jako dekorator funkcji'''
# import random
#
# wszystkie_produkty = ["sukienka", "podkoszulek", "skarpetki", "spodnie", "spodnica", "szalik", "koszula", "pasek"]
#
#
# class Losowanie:
#
#     wybrane_dzisiaj = []
#
#     def __init__(self, func):
#         self.func = func
#
#
#     def __call__(self, produkty):
#         produkty_do_losowania = [x for x in produkty if x not in Losowanie.wybrane_dzisiaj]
#         produkt = self.func(produkty_do_losowania)
#         Losowanie.wybrane_dzisiaj.append(produkt)
#         return produkt
#
#
# @Losowanie
# def znizka30(produkty):
#     return random.choice(produkty)
#
#
# @Losowanie
# def znizka50(produkty):
#     return random.choice(produkty)
#
#
# @Losowanie
# def dwa_za_jeden(produkty):
#     return random.choice(produkty)
#
#
# print("PROMOCJE NA DZISIAJ")
# print("- 30% na wszystkie {}".format(znizka30(wszystkie_produkty)))
# print("- 50% na wszystkie {}".format(znizka50(wszystkie_produkty)))
# print("Dwa w cenie jednego {}".format(dwa_za_jeden(wszystkie_produkty)))

''''''

#
# class Cake:
#     bakery_offer = []
#
#     def __init__(self, name, kind, taste, additives, filling):
#
#         self.name = name
#         self.kind = kind
#         self.taste = taste
#         self.additives = additives.copy()
#         self.filling = filling
#         self.bakery_offer.append(self)
#
#     def show_info(self):
#         print("{}".format(self.name.upper()))
#         print("Kind:        {}".format(self.kind))
#         print("Taste:       {}".format(self.taste))
#         if len(self.additives) > 0:
#             print("Additives:")
#             for a in self.additives:
#                 print("\t\t{}".format(a))
#         if len(self.filling) > 0:
#             print("Filling:     {}".format(self.filling))
#         print('-' * 20)
#
#     def add_additives(self, additives):
#         self.additives.extend(additives)
#
#
# class NoDuplicates:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, cake, additives):
#         no_duplicate_list = cake.additives
#         for x in additives:
#             if x not in no_duplicate_list:
#                 no_duplicate_list.append(x)
#         return no_duplicate_list
#
#
# cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
#
#
# @NoDuplicates
# def add_extra_additives(cake, additives):
#     cake.add_additives(additives)
#
#
# add_extra_additives(cake01, ['strawberries', 'sugar-flowers'])
# cake01.show_info()
#
# add_extra_additives(cake01, ['strawberries', 'sugar-flowers', 'chocolade', 'nuts'])
# cake01.show_info()


'''operatory'''


# class Cake:
#     bakery_offer = []
#
#     def __init__(self, name, kind, taste, additives, filling):
#
#         self.name = name
#         self.kind = kind
#         self.taste = taste
#         self.additives = additives.copy()
#         self.filling = filling
#         self.bakery_offer.append(self)
#
#     def show_info(self):
#         print("{}".format(self.name.upper()))
#         print("Kind:        {}".format(self.kind))
#         print("Taste:       {}".format(self.taste))
#         if len(self.additives) > 0:
#             print("Additives:")
#             for a in self.additives:
#                 print("\t\t{}".format(a))
#         if len(self.filling) > 0:
#             print("Filling:     {}".format(self.filling))
#         print('-' * 20)
#
#     def __str__(self):
#         return '{} - {} addivites: {}'.format(self.name, self.kind, self.additives)
#
#     def __iadd__(self, other):
#         if type(other) is list:
#             new_addivites = self.additives
#             new_addivites.extend(other)
#             return Cake(self.name, self.kind, self.taste, new_addivites, self.filling)
#         elif type(other) is str:
#             new_addivites = self.additives
#             new_addivites.append(other)
#             return Cake(self.name, self.kind, self.taste, new_addivites, self.filling)
#         else:
#             raise Exception("Niepoprawny składnik")
#
#
# cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
# print(cake01)
#
# cake01 += "vanilla"
# print(cake01)
#
# cake01 += ["rum", "coco"]
# print(cake01)


'''dziedziczenie'''


# class Cake:
#     bakery_offer = []
#
#     def __init__(self, name, kind, taste, additives, filling):
#
#         self.name = name
#         self.kind = kind
#         self.taste = taste
#         self.additives = additives.copy()
#         self.filling = filling
#         self.bakery_offer.append(self)
#
#     def show_info(self):
#         print("{}".format(self.name.upper()))
#         print("Kind:        {}".format(self.kind))
#         print("Taste:       {}".format(self.taste))
#         if len(self.additives) > 0:
#             print("Additives:")
#             for a in self.additives:
#                 print("\t\t{}".format(a))
#         if len(self.filling) > 0:
#             print("Filling:     {}".format(self.filling))
#
#
#     def __str__(self):
#         return "--== {} - {} ==--".format(self.name.upper(), self.kind)
#
#
# class SpecialCake(Cake):
#     def __init__(self, name, kind, taste, additives, filling, occasion, shape, ornaments, text):
#         Cake.__init__(self, name, kind, taste, additives, filling)
#         self.occasion = occasion
#         self.shape = shape
#         self.ornaments = ornaments
#         self.text = text
#
#     def show_info(self):
#         Cake.show_info(self)
#         print("Occasion: {}".format(self.occasion))
#         print("Shape: {}".format(self.shape))
#         print("Ornaments: {}".format(self.ornaments))
#         if len(self.text) > 0:
#             print("Text on cake: {}".format(self.text))
#         print('-' * 20)
#
#
# birthday = SpecialCake("Birthady cake", "cake", "chocolate", ["nuts"], "chocolate", "birthady", "square", "rose", "happy birthady")
# wedding = SpecialCake("Weadding cake", "cake", "creamy", ["coco"], "creamy", "wedding", "round", "rose", "")
# print(birthday)
# print(birthday.show_info())
# print(wedding)
# print(wedding.show_info())


'''Dziedziczenie wielokrotne'''


# class Animal:
#
#     def __init__(self, name, year, breed):
#         self.name = name
#         self.year = year
#         self.breed = breed
#         self.all_name = "{} ({}) - {}".format(self.name, self.year, self.breed)
#
#     def PrintInformation(self):
#         return "Name: {} \nbreed: {} \nyear {}".format(self.name, self.breed, self.year)
#
#
# class Person:
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.all_name = "{} {}".format(self.first_name, self.last_name)
#
#     def PrintInformation(self):
#         return "Person: {} {}".format(self.first_name, self.last_name)
#
#
# class AdoptionAnimal(Animal, Person):
#
#     def __init__(self,  animal, person):
#         Person.__init__(self, person.first_name, person.last_name)
#         Animal.__init__(self, animal.name, animal.year, animal.breed)
#
#     def PrintInformation(self):
#         return "Animal: {}\nOwner: {} {}".format(self.all_name, self.first_name, self.last_name)
#
#
# animal = Animal("Eevee", "2019", "Rabbit")
# person = Person("Justyna", "Zaczyk")
# adoption = AdoptionAnimal(animal, person)
# print(adoption.PrintInformation())
# print(vars(adoption))
# print(AdoptionAnimal.__mro__)


''''''

# from datetime import date
# from datetime import timedelta
#
#
# class Cake:
#     bakery_offer = []
#
#     def __init__(self, name, kind, taste, additives, filling):
#
#         self.name = name
#         self.kind = kind
#         self.taste = taste
#         self.additives = additives.copy()
#         self.filling = filling
#         self.bakery_offer.append(self)
#
#     def show_info(self):
#         print("{}".format(self.name.upper()))
#         print("Kind:        {}".format(self.kind))
#         print("Taste:       {}".format(self.taste))
#         if len(self.additives) > 0:
#             print("Additives:")
#             for a in self.additives:
#                 print("\t\t{}".format(a))
#         if len(self.filling) > 0:
#             print("Filling:     {}".format(self.filling))
#         print('-' * 20)
#
#     @property
#     def full_name(self):
#         return "--== {} - {} ==--".format(self.name.upper(), self.kind)
#
#
# class Promo:
#
#     def __init__(self, name, discount, start_date, end_date, minimal_order):
#         self.name = name
#         self.discount = discount
#         self.start_date = start_date
#         self.end_date = end_date
#         self.minimal_order = minimal_order
#
#     @property
#     def full_name(self):
#         return "PROMO {0:s} {1:.0%}".format(self.name, self.discount)
#
#
# class PromoCake(Cake, Promo):
#
#     def __init__(self, cake, promo):
#         Cake.__init__(self, cake.name, cake.kind, cake.taste, cake.additives, cake.filling)
#         Promo.__init__(self, promo.name, promo.discount, promo.start_date, promo.end_date, promo.minimal_order)
#
#
# cake = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
# cake.show_info()
#
# promo10 = Promo("DISCOUNT - no additional conditions", 0.15, date.today(), date.today() + timedelta(days=14), 0)
# print(promo10.full_name)
#
# promo_cake = PromoCake(cake, promo10)
# print(promo_cake.show_info())
# print(promo_cake.full_name)