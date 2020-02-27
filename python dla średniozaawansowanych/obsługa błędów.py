'''wprowadzenie'''

# import requests
# import os
# import shutil
#
#
# def save_url_to_file(url, file_path):
#     r = requests.get(url, stream=True)
#     with open(file_path, "wb") as f:
#         f.write(r.content)
#
#
# url = 'http://www.mobilo24.eu/spis/'
# tmpfile = 'download.tmp'
# file = 'spis.html'
#
# file_path = tmpfile
#
# try:
#     if os.path.isfile(tmpfile):
#         os.remove(tmpfile)
#     save_url_to_file(url, tmpfile)
#
#     shutil.copy(file, "download.tmp")
#
# except ConnectionError as e:
#     print("Podano nieprawidłowy adres")
#
# except PermissionError as e:
#     print("Niepoprawny tryb odczytu, wpisz wb")
#
# except FileNotFoundError as e:
#     print("Pliku nie można skopiować gdyż nie istnieje")
#
# except Exception as e:
#     print("Doszlo do błędu: ", e)
#
# else:
#     print("Zakończono bez błędu")
#
# finally:
#     if os.path.isfile(tmpfile):
#         os.remove(tmpfile)
#         print("Plik został usunięty")
#     else:
#         print("Zakonczono działanie")


'''Samodzielnie zgłaszanie błędów'''
# import datetime as dt
#
#
# class Trip:
#     def __init__(self, symbol, title, start, end):
#         self.symbol = symbol
#         self.title = title
#         self.start = start
#         self.end = end
#
#     def check_data(self):
#         if len(self.title) == 0:
#             raise Exception("Title is empty!")
#         if self.start > self.end:
#             raise ValueError("Start date is later than end date!")
#
#
#
# trips = [
#     Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
#     Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
#     Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
# ]
#
# def publish_offer(trips):
#     list_of_errors = []
#     for t in trips:
#         try:
#             t.check_data()
#         except ValueError:
#             list_of_errors.append("<{}>: <ValueError>".format(t.symbol))
#         except Exception:
#             list_of_errors.append("<{}>: <Exception>".format(t.symbol))
#
#     if len(list_of_errors) != 0:
#         raise Exception("The list of trips has errors: {}".format(list_of_errors))
#     else:
#         print("the offer will be published...")
#
# try:
#     print("START")
#     publish_offer(trips)
#     print("DONE")
# except Exception as e:
#     print("ERROR", e)

'''metoda assert'''

# import datetime as dt
# import sys
#
#
# class Trip:
#     def __init__(self, symbol, title, start, end):
#         self.symbol = symbol
#         self.title = title
#         self.start = start
#         self.end = end
#
#     def check_data(self):
#         assert len(self.title) != 0, "Title is empty!"
#         assert self.start <= self.end, "Start date is later than end date!"
#
#
# trips = [
#     Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
#     Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
#     Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
# ]
#
# def publish_offer(trips):
#     list_of_errors = []
#     for t in trips:
#         try:
#             t.check_data()
#         except ValueError:
#             list_of_errors.append("<{}>: <ValueError>".format(t.symbol))
#         except Exception:
#             list_of_errors.append("<{}>: <Exception>".format(t.symbol))
#
#     assert len(list_of_errors) == 0, "The list of trips has errors: {}".format(list_of_errors)
#
#     return True
#
#
# try:
#     print("START")
#     publish_offer(trips)
#     print("DONE")
# except Exception as e:
#     print("ERROR", e)

'''Definiowanie własnych wyjątków'''


# class BITException(Exception):
#     def __init__(self, text, area):
#         super().__init__(text)
#         self.area = area
#
#     def __str__(self):
#         return "{} area: {}".format(super().__str__(), self.area)
#
#
# class BITSecurityException(BITException):
#     pass
#
#
# class BITDataFormatException(BITException):
#     pass
#
#
# try:
#     #do something...
#     raise BITException("file format is icorrect", "Pinancial data")
# except BITSecurityException as e:
#     print("Aplication seciurity error: {}".format(e))
# except BITDataFormatException as e:
#     print("Aplication data malformed error: {}".format(e))
# except BITException as e:
#     print("Aplication error: {}".format(e))
# except Exception as e:
#     print("Grneral error: {}".format(e))
#
#
# # try:
# #     #do something...
# #     raise BITException("file format is icorrect", "Pinancial data")
# # except BITException as e:
# #     print("Aplication error: {}, area: {}".format(e, e.area))


''''''


import datetime as dt

class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        if len(self.title) == 0:
            raise TripNameException
        if self.start > self.end:
            raise TripDateException("The list of trips has errors")

    @classmethod
    def publish_offer(cls, trips):

        list_of_errors = []

        for trip in trips:
            try:
                trip.check_data()
            except TripNameException as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
            except TripDateException as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))

        if len(list_of_errors) > 0:
            raise TripException("The list of trips has errors", list_of_errors)
        else:
            print('the offer will be published...')


class TripException(Exception):
    def __init__(self, text, description):
        super().__init__(text)
        self.description = description

    def __str__(self):
        return "{}, info: {}".format(super().__str__(), self.description )


class TripNameException(TripException):
    def __init__(self, text):
        super().__init__(text, 'Name of the trip is missing. You need to name the trip somehow...')


class TripDateException(TripException):
    def __init__(self, text):
        super().__init__(text, 'The dates are incorrect. The starting date should be earlier than the ending date...')


trips = [
            Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
            Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
            Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
        ]


try:
    print('Publishing trips...')
    Trip.publish_offer(trips)
    print('... done')
except Exception as e:
    print('THERE ARE ERRORS')
    print(e)
    print('THE OFFER CANNOT BE PUBLISHED')