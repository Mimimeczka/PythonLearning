'''świat bez klas'''
# cake_1 = {"taste": 'vanilia', "glaze": 'chocolade', "text": 'Happy Brithday', "weight": 0.7}
# cake_2 = {"taste": 'tee', "glaze": 'lemon', "text": 'Happy Python Coding', "weight": 1.3}
#
#
# def show_cake_info(cake):
#     print('{} cake with {} glaze with text "{}" of {} kg'.format(
#         cake["taste"], cake["glaze"], cake["text"], cake["weight"]))
#
#
# all_cake = [cake_1, cake_2]
#
# for x in all_cake:
#     print(show_cake_info(x))

'''klasy i atrybuty instancji klasy'''
import pickle
import glob
import types


def export_this_cake_to_html(self, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(self.name, self.kind, self.taste, self.addictions, self.filing)
        f.write(content)

def export_all_cake_to_html(cls, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        for obj in cls.bakery_offer:
            content = template.format(obj.name, obj.kind, obj.taste, obj.addictions, obj.filing)
            f.write(content)


class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, addictions, filing, gluten_free, text):
        self.__gluten_free = gluten_free
        self.name = name
        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = "other"
        self.taste = taste
        self.addictions = addictions
        self.filing = filing
        self.__text = text
        Cake.bakery_offer.append(self)


    def show_info(self):
        print("{} - ({})".format(self.name.upper(), self.kind))
        print("Taste:", self.taste)
        if len(self.addictions) > 0:
            print("Addivites:", self.addictions)
        if len(self.filing) > 0:
            print("Filings:", self.filing)
        print("Gluten free: ", self.__gluten_free)
        if self.kind == "cake" and self.__text != "":
            print("Text on cake:", self.__text)
        print("-" * 20)


    def set_filling(self, filling):
        self.filing += (", " + filling)

    def add_additives(self, addictions):
        self.addictions += (", " + addictions)

    @property
    def set_text(self):
        return self.__text

    @set_text.setter
    def set_text(self, new_text):
        if self.kind == "cake":
            self.__text = new_text
            return "Text on cake: {}".format(self.__text)
        else:
            return "This isn't cake!!"

    @set_text.deleter
    def set_text(self):
        self.__text = ""

    def save_to_file(self, path):
        with open(path, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def read_from_file(cls, path):
        with open(path, "rb") as file:
            new_obj = pickle.load(file)
            cls.bakery_offer.append(new_obj)
        return new_obj

    @staticmethod
    def get_bakery_files(path):
        return glob.glob(path + '/*.bakery')



bun = Cake("strawberry bun", "bun", "strawberry", "white chocolate", "", True, "")
cake = Cake("birthady cake", "cake", "chocolate", "toffie, nuts", "", False, "")

cake._Cake__gluten_free = True

bun.set_filling("strawberry")
bun.add_additives("strawberry, coco")

cake.set_text ="Happy Birthady"
bun.set_text ="Happy Birthady"

del cake.set_text   

bun.save_to_file("babeczka.bakery")
cake.save_to_file("ciasto.bakery")

bunn = bun.read_from_file("babeczka.bakery")
cakee = cake.read_from_file("ciasto.bakery")

print(Cake.get_bakery_files("."))

print("Today in our offer:")
print("*" * 20)
for x in Cake.bakery_offer:
    x.show_info()


Cake.export_all = types.MethodType(export_all_cake_to_html, Cake)
Cake.export_all(path="piekarnia.html")


for x in Cake.bakery_offer:
    Cake.export_this = types.MethodType(export_this_cake_to_html, x)
    Cake.export_this(path=str(x.name) + ".html".replace(" ", "_"))
    print(x.name.replace(" ", "_"))


''''''
# '''Zmienne: HowManyCars = 0 ListCars = [] są zdefiniowane na poziomie klasy NIE instancji'''
# class Car:
#     HowManyCars = 0
#     ListCars = []
#
#     def __init__(self, brand, mmodel):
#         self.brand = brand
#         self.model = mmodel
#         Car.HowManyCars += 1
#         Car.ListCars.append(self)
#
# print("Liczba poswstałych samochodów:", Car.HowManyCars)
# print("Pokaż samochody:", Car.ListCars)

'''Ukrywanie atrybutów klasy'''

# class Foo:
#     def __init__(self, name):
#         self.__name = name
#
#     def PrintInformation(self):
#         print(self.__name)
#
# obiekt = Foo("Eevee")
# obiekt.PrintInformation()
# print(vars(obiekt))
# print("-" * 20)
# obiekt.__name = "Krolik"
# obiekt.PrintInformation()
# print(vars(obiekt))
# print("-" * 20)
# obiekt._Foo__name = "Krolik"
# obiekt.PrintInformation()
# print(vars(obiekt))
# print("-" * 20)
# del obiekt.__name
# obiekt.PrintInformation()
# print(vars(obiekt))
# print("-" * 20)
# setattr(obiekt, "ssak", True)
# obiekt.PrintInformation()
# print(vars(obiekt))
# print("-" * 20)
# print(hasattr(obiekt, "ssak")) # czy istnieje obiekt o atrybucie
# obiekt.PrintInformation()
# print(vars(obiekt))
# print("-" * 20)
# delattr(obiekt, "ssak")
# obiekt.PrintInformation()
# print(vars(obiekt))
'''Ukrywanie atrybutu odbywa se na zasadzie doklejenia przed ukrywanym atrybutem _ i nazwe obiektu.
Zostaje tworzona nowa właściwosc ale to nie jest ta sama zdefiniowana wewnętrznie w klasie.
Teraz ten obiekt posiada nowy atrybut __name = Krolik. 
Pomimo iż atrybut jest ukryty to da się go zmodyfikowa z zewnątrz klasy
Pythonowe klasy niestety słabo się bronią przed zewnętrznymi ich modyfikacjami. 
Polecenie del powoduje usunięcie wybranego atrybutu.
Klase w Pythonie można modyfikowa w trakcie życia obiektu.
Nawet istnieją do tego metody'''


'''właściwości klasy'''

# edit_on_sale = False
#
# class Foo:
#     def __init__(self, name, on_sale):
#         self.__name = name
#         self.__on_sale = on_sale
#
#     def PrintInformation(self):
#         print(self.__name)
#         print("On sale:", self.__on_sale)
#
#     def Get_on_sale(self):
#         return self.__on_sale
#
#     def Set_on_sale(self, new_on_sale):
#         if self.__on_sale == edit_on_sale:
#             self.__on_sale = new_on_sale
#         return "On sale: {}".format(self.__on_sale)
#
#
#     IsOnSale = property(Get_on_sale, Set_on_sale, None, "zmieniono")
#
#
#
# obiekt = Foo("Eevee", False)
# obiekt.PrintInformation()
# # print(obiekt.Get_on_sale())
# # print(obiekt.Set_on_sale(True))
# # obiekt.PrintInformation()
# obiekt.IsOnSale = True
# obiekt.PrintInformation()


'''Metody klasy i metody statyczne'''


# class Foo:
#     def __init__(self, name, on_sale):
#         self.__name = name
#         self.__on_sale = on_sale
#
#     def PrintInformation(self):
#         print(self.__name)
#         print("On sale:", self.__on_sale)
#
#     @classmethod
#     def ReadText(cls, text):
#         new_animal = cls(*text.split(", "))
#         return new_animal
#
#     @staticmethod
#     def HowManyYear(x):
#         if x == 0.5:
#             return "15 Year"
#         elif x == 1:
#             return "25 Year"
#         elif x == 3:
#             return "33 Year"
#         elif x == 5:
#             return "49 Year"
#         elif x == 6:
#             return "57 Year"
#         elif x == 7:
#             return "65 Year"
#         elif x == 8:
#             return "73 Year"
#         elif x == 9:
#             return "80 Year"
#         elif x == 10:
#             return "88 Year"
#         else:
#             return "None"
#
#
# text = "Kicaj, True"
# obiekt_text = Foo.ReadText(text)
# obiekt_text.PrintInformation()
#
# year = Foo.HowManyYear(5)
# print(year)
#
# print(obiekt_text.ReadText(text))
# print(obiekt_text.HowManyYear(7))
#
# import pickle
# import glob
#
# with open("test", "wb") as file:
#     pickle.dump(obiekt_text, file)
#
# with open("test", "rb") as file:
#     x = pickle.load(file)
#
# x.PrintInformation()
#
# files = glob.glob("/Users/justyna/Desktop/przepisy/s*.*")
# print(files)


'''Tworzenie właściwości za pomocą dekoratorów'''


# edit_on_sale = False
#
# class Foo:
#     def __init__(self, name, on_sale):
#         self.__name = name
#         self.__on_sale = on_sale
#
#     def PrintInformation(self):
#         print(self.__name)
#         print("On sale:", self.__on_sale)
#
#     # def Is_On_Sale(self):
#     #     return self.__on_sale
#
#     @property
#     def Is_On_Sale(self):
#         return self.__on_sale
#
#     @Is_On_Sale.setter
#     def Is_On_Sale(self, new_on_sale):
#         if self.__on_sale == edit_on_sale:
#             self.__on_sale = new_on_sale
#         print("On sale: {}".format(self.__on_sale))
#
#     @Is_On_Sale.deleter
#     def Is_On_Sale(self):
#         self.__on_sale = None
#
#     @property
#     def Title(self):
#         return "Name: {}, on sale: {}".format(self.__name, self.__on_sale).title()
#
# obiekt = Foo("Eevee", False)
# obiekt.PrintInformation()
# # print(obiekt.Is_On_Sale())
# print(obiekt.Is_On_Sale)
# obiekt.Is_On_Sale = True
# print(obiekt.PrintInformation())
# del obiekt.Is_On_Sale
# print(obiekt.PrintInformation())
# print(obiekt.Title)


'''dynamicznie dodawane metody doklasy'''
# import csv
# import types
#
#
# def ExportToFile(self, path):
#     with open(path, mode="w") as file:
#         writer = csv.writer(file, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
#         writer.writerow(["name", "on_sale"])
#         writer.writerow([self.name, self.on_sale])
#     print("This is function ExportToFile - instance method")
#
#
# edit_on_sale = False
#
#
# class Foo:
#     list_of_object = []
#
#     def __init__(self, name, on_sale):
#         self.name = name
#         self.on_sale = on_sale
#         Foo.list_of_object.append(self)
#
#     def PrintInformation(self):
#         print(self.name)
#         print("On sale:", self.on_sale)
#
#     def Get_on_sale(self):
#         return self.on_sale
#
#     def Set_on_sale(self, new_on_sale):
#         if self.on_sale == edit_on_sale:
#             self.on_sale = new_on_sale
#         return "On sale: {}".format(self.on_sale)
#
#
#     IsOnSale = property(Get_on_sale, Set_on_sale, None, "zmieniono")
#
# obiektA = Foo("Eevee", False)
# obiektB = Foo("Futrzak", True)
#
# Foo.export_to_file = types.MethodType(ExportToFile, obiektA)
# Foo.export_to_file(path="instance.csv")
# print(dir(Foo))
#
# if hasattr(obiektA, "export_to_file") and callable(obiektA.export_to_file):
#     print("This object has method export_to_file")
# if hasattr(obiektA, "ExportToFile") and callable(obiektA.ExportToFile):
#     print("This object has method ExportToFile")