'''wprowadzenie'''
# import time
#
#
# class TimeMeasure:
#
#     def __init__(self):
#         pass
#
#     def __enter__(self):
#         print("entering...")
#         self.__start = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("exiting...")
#         self.__exit = time.time()
#         self.__time = self.__exit - self.__start
#         print("Execution time {}".format(self.__time))
#         return
#
#
# with TimeMeasure() as my_time:
#     time.sleep(3)

''''''
# import time
#
#
# class TimeMeasure:
#
#     def __init__(self):
#         pass
#
#     def __enter__(self):
#         print('''
# <TABLE>
# <TR>
#     <TH>Number</TH><TH>Description</TH>
# </TR>''')
#         self.__start = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("</TABLE>")
#         self.__exit = time.time()
#         self.__time = self.__exit - self.__start
#         print("Execution time {}".format(self.__time))
#         return
#
#
# with TimeMeasure() as my_time:
#     print('''
# <TR>
#     <TD>1</TD><TD>Say hello!</TD)
# </TR>
# <TR>
#     <TD>2</TD><TD>Say good bye!</TD)
# </TR>''')

'''plik ini'''
# import os
#
# class IniFile:
#     def __init__(self, path):
#         self.path = path
#         self.parameters = {}
#         self.read_from_disk()
#
#     def read_from_disk(self):
#         if os.path.isfile(self.path):
#             with open(self.path) as file:
#                 for line in file:
#                     if "=" in line:
#                         parts = line.replace("\n", '').split("=")
#                         self.parameters[parts[0]] = parts[1]
#
#     def read_parameters(self, key):
#         if key in self.parameters.keys():
#             return self.parameters[key]
#         else:
#             return None
#
#     def write_parameters(self, key, values):
#         self.parameters[key] = values
#
#     def save_on_disk(self):
#         with open(self.path, "w") as file:
#             for key, values in self.parameters.items():
#                 line = "{} = {} \n".format(key, values)
#                 file.writelines(line)
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#
#
# with IniFile("pliki_ini.txt") as file:
#     file.write_parameters("klucz", "wartosc")
#     file.write_parameters("klucz kolejny", "wartosc kolejna")
#     print(file.parameters)
#     print(file.read_parameters("klucz"))
#
# # przykladA = IniFile("pliki_ini.txt")
# # przykladA.write_parameters("klucz", "wartosc")
# # przykladA.write_parameters("klucz kolejny", "wartosc kolejna")
# # przykladA.save_on_disk()
# # print(przykladA.read_parameters("klucz"))
# # print(przykladA.read_parameters("klucz kolejny"))
# # print(przykladA.parameters)

''''''

# import os
# import zipfile
# import requests
#
#
# class FileFromWeb:
#     def __init__(self, url, temp_file):
#         self.url = url
#         self.temp_file = temp_file
#
#     def __enter__(self):
#         response = requests.get(self.url)
#         with open(self.temp_file, "wb") as file:
#             file.write(response.content)
#             return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#
#
# with FileFromWeb("https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip", "euroxref.zip") as f:
#     with zipfile.ZipFile("f.tmp_file", "f") as z:
#         a_file = z.namelist()[0]
#         print(a_file)
#         # os.chdir('c:/temp')
#         z.extract(a_file, '.', None)


'''obsługa błędów w context manager'''
import os

class IniFile:
    def __init__(self, path):
        self.path = path
        self.parameters = {}
        self.read_from_disk()

    def read_from_disk(self):
        if os.path.isfile(self.path):
            with open(self.path) as file:
                for line in file:
                    if "=" in line:
                        parts = line.replace("\n", '').split("=")
                        self.parameters[parts[0]] = parts[1]

    def read_parameters(self, key):
        if key in self.parameters.keys():
            return self.parameters[key]
        else:
            return None

    def write_parameters(self, key, values):
        self.parameters[key] = values

    def save_on_disk(self):
        with open(self.path, "w") as file:
            for key, values in self.parameters.items():
                line = "{}={} \n".format(key, values)
                file.writelines(line)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exc_type = ", exc_type)
        print("exc_val = ", exc_val)
        print("exc_tb = ", exc_tb)
        if exc_type == OSError:
            return False
        else:
            return True


with IniFile("pliki_ini.txt") as file:
    file.write_parameters("klucz", "wartosc")
    file.write_parameters("klucz kolejny", "wartosc kolejna")
    file.write_parameters("klucz kolejny dwa", "wartosc kolejna dwa")
    file.save_on_disk()
    print(file.parameters)

''''''


# import os
# import zipfile
# import requests
#
#
# class FileFromWeb:
#     def __init__(self, url, temp_file):
#         self.url = url
#         self.temp_file = temp_file
#
#     def __enter__(self):
#         response = requests.get(self.url)
#         with open(self.temp_file, "wb") as file:
#             file.write(response.content)
#             return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type == FileNotFoundError or exc_type == KeyError:
#             print("Doszlo do bledu ", exc_type)
#         else:
#             return False
#
#
# with FileFromWeb("https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip", "euroxref.zip") as f:
#     with zipfile.ZipFile("f.tmp_file", "f") as z:
#         a_file = z.namelist()[0]
#         print(a_file)
#         # os.chdir('c:/temp')
#         z.extract(a_file, '.', None)

'''moduł contextlib'''

# from contextlib import contextmanager
#
# class Door:
#     def __init__(self, where):
#         self.where = where
#
#     def open(self):
#         print("Opening door to the: {}".format(self.where))
#
#     def close(self):
#         print("Closing door to the: {}".format(self.where))
#
#
# @contextmanager
# def OpenAndClose(object):
#     object.open()
#     yield object
#     object.close()
#
#
# with OpenAndClose(Door("room")) as door:
#     print("The dor is to the {}".format(door.where))


''''''

# from contextlib import contextmanager
#
# class Door:
#     def __init__(self, where):
#         self.where = where
#
#     def open(self):
#         print("Opening door to the: {}".format(self.where))
#
#     def close(self):
#         print("Closing door to the: {}".format(self.where))
#
#
# @contextmanager
# def OnlyClose(object):
#
#     yield object
#     object.close()
#
# with OnlyClose(Door("room")) as door:
#     door.close()
#     print("The dor is to the {}".format(door.where))

''''''

# from urllib.request import urlopen
# from contextlib import closing
#
# with closing(urlopen('http://kursyonline24.eu')) as page:
#     for line in page:
#         print(line)

''''''
# import os
# import contextlib
#
# with contextlib.suppress(FileNotFoundError):
#     os.remove("test")

''''''
# class Door:
#     def __init__(self, where):
#         self.where = where
#
#     def open(self):
#         print("Opening door to the: {}".format(self.where))
#
#     def close(self):
#         print("Closing door to the: {}".format(self.where))
#
#
# from contextlib import redirect_stdout
# f = open("przebieg_funkcji.txt", "w")
# with redirect_stdout(f):
#     print("Hello")
#     door = Door("room")
#     door.open()
#     door.close()

''''''

# import os
# import zipfile
# import requests
# import contextlib
#
#
# class FileFromWeb:
#
#     def __init__(self, url, tmp_file):
#         self.url = url
#         self.tmp_file = tmp_file
#
#     def download_file(self):
#         response = requests.get(self.url)
#         with open(self.tmp_file, 'wb') as f:
#             f.write(response.content)
#         return self
#
#     def close(self):
#         if os.path.isfile(self.tmp_file):
#             os.remove(self.tmp_file)
#
#
# with contextlib.suppress(FileNotFoundError):
#     with contextlib.closing(FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'euroxref1.zip')) as f:
#             f.download_file()
#
#             with zipfile.ZipFile(f.tmp_file, 'r') as z:
#                 a_file = z.namelist()[0]
#                 print(a_file)
#                 # os.chdir('c:/temp')
#                 # z.extract(a_file, '.', None)

