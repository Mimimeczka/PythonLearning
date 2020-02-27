'''wrapper dla funkcji dekorowanie funkcji'''

# import functools
# import datetime
#
# def CreateFunctionWithWrapper(func):
#     def func_with_wrapper(*args, **kwargs):
#         print("Funkcja: {} została wywołana {}". format(func.__name__, datetime.datetime.now()))
#         print("Użyto w tej funkcji następujących argumentów:")
#         for x in args:
#             print(x)
#         for y in kwargs:
#             print(y, "-", kwargs[y])
#         print("Wywołanie funkcji:")
#         result = func(*args, **kwargs)
#         print("Wywołana funkcja zwraca:", result)
#         return result
#     return func_with_wrapper
#
#
# @CreateFunctionWithWrapper
# def ChangeSalary(pracownik, nowe_wynagrodzenie, bonus=False):
#     print("Pracownik: {} wynagrodzenie {} bonus jednorazowy {}" .format(pracownik, nowe_wynagrodzenie, bonus))
#     return nowe_wynagrodzenie
#
# przyklad = ChangeSalary("Jan Kowalski", 2000, bonus=False)
# print(przyklad)

''''''

# import time
# import functools
#
# def wrapper_time(function):
#     start = time.time()
#     def a_wrapped_function(x):
#         y = function(x)
#         return y
#     end = time.time()
#     print(f"Czas trwania funkcji: {end - start}")
#     return a_wrapped_function
#
#
# @wrapper_time
# def get_sequence(n):
#     if n <= 0:
#         return 1
#     else:
#         v = 0
#         for i in range(n):
#             v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
#         return v
#
#
# # print(get_sequence(18))
# print(get_sequence(19))
# # print(get_sequence(20))

'''Funkcja wrapper z parametrami'''
# import functools
# import datetime
# # LongFilePath = f"wrapper z parametrami"
#
# def CreateFunctionWithWrapper_LongFile(LongFilePath):
#     def CreateFunctionWithWrapper(func):
#         def func_with_wrapper(*args, **kwargs):
#             file = open(LongFilePath, "a")
#             file.write("-" * 20 + "\n")
#             file.write("Funkcja: {} została wywołana {}\n". format(func.__name__, datetime.datetime.now()))
#             file.write("Użyto w tej funkcji następujących argumentów:\n")
#             file.write(" ".join("{}". format(x) for x in args))
#             file.write("\n")
#             file.write(" ".join("{} - {}".format(x, kwargs[x]) for x in kwargs))
#             file.write("\n")
#             result = func(*args, **kwargs)
#             file.write("Wywołana funkcja zwraca:\n")
#             file.write("{}\n".format(result))
#             file.close()
#             return result
#         return func_with_wrapper
#     return CreateFunctionWithWrapper
#
#
# @CreateFunctionWithWrapper_LongFile("wrapper z parametrami")
# def ChangeSalary(pracownik, nowe_wynagrodzenie, bonus=False):
#     print("Pracownik: {} wynagrodzenie {} bonus jednorazowy {}" .format(pracownik, nowe_wynagrodzenie, bonus))
#     return nowe_wynagrodzenie
#
# przyklad = ChangeSalary("Jan Kowalski", 2000, bonus=False)
# print(przyklad)

''''''
# import os
# from datetime import datetime as dt
# import functools
#
# def wrapper_with_log_file(logged_action, log_file_path):
#     def wrapper_with_log_to_known_file(func):
#         def fthe_real_wrapper(path):
#             file = open(log_file_path, "a")
#             file.write("Action {} excutend on {} on {}".format(logged_action, path, dt.now().strftime("%Y-%m-%d %H:%M:%S")))
#             file.write("\n")
#             file.close()
#             return func(path)
#         return fthe_real_wrapper
#     return wrapper_with_log_to_known_file
#
#
#
#
# @wrapper_with_log_file("FILE_CREATE", "create.txt")
# def create_file(path):
#     print('creating file {}'.format(path))
#     open(path, "w+")
#
# @wrapper_with_log_file("DELETE_CREATE","delete.txt")
# def delete_file(path):
#     print('deleting file {}'.format(path))
#     os.remove(path)
#
#
# create_file(r'c:\temp\dummy_file.txt')
# delete_file(r'c:\temp\dummy_file.txt')
# create_file(r'c:\temp\dummy_file.txt')
# delete_file(r'c:\temp\dummy_file.txt')

'''wysyłanie maili z pythona'''

# import sys
# import smtplib
#
# mailFrom = 'Your automation system'
# mailTo = "justyna.zaczyk@onet.pl"
# mailSubject = 'Processing finished successfully'
# mailBody = '''Hello
#
# This mail confirms that processing has finished without problems,
#
# Have a nice day!'''
#
# message = '''From: {}
# Subject: {}
#
# {}
# '''.format(mailFrom, mailSubject, mailBody)
#
# user = "justynaa.zaczyk@gmail.com"
# password = "xxx"
#
# try:
#     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     server.ehlo()
#     server.login(user, password)
#     server.sendmail(user, mailTo, message)
#     server.close()
#     print('mail sent')
# except:
#     print('error sending email', sys.exc_info()[0])

'''funkcja partial'''

# import sys
# import smtplib
# import functools
#
# def SendInfoMail(user, password, mailFrom, mailTo, mailSubject, mailBody):
#     message = '''From: {}
# Subject: {}
# {}
# '''.format(mailFrom, mailSubject, mailBody)
#
#     try:
#         server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#         server.ehlo()
#         server.login(user, password)
#         server.sendmail(user, mailTo, message)
#         server.close()
#         return 'mail sent'
#     except:
#         return 'error sending email', sys.exc_info()[0]
#
#
# mailFrom = 'Your automation system'
# mailTo = "justyna.zaczyk@onet.pl"
# mailSubject = 'Processing finished successfully'
# user = "justynaa.zaczyk@gmail.com"
# password = "xxx"
# mailBody = '''Hello
# This mail confirms that processing has finished without problems,
# Have a nice day!'''
#
# print(SendInfoMail(user, password, mailFrom, mailTo, mailSubject, mailBody))
#
# SendInfoMailFromGmail = functools.partial(SendInfoMail, user, password)
# print(SendInfoMailFromGmail(mailFrom, mailTo, mailSubject,   mailBody))
#
# SendInfoMailFromGmail = functools.partial(SendInfoMail, user, password,  mailSubject="Execution alert")
# print(SendInfoMailFromGmail(mailFrom=mailFrom, mailTo=mailTo, mailBody=mailBody))

''''''

# import requests
# import os
# import functools
#
# def save_url_file(url, file, msg):
#     print(msg.format(file))
#
#     r = requests.get(url, stream=True)
#     file_path = os.path.join(file)
#
#     with open(file_path, "wb") as f:
#         f.write(r.content)
#
#
# msg = "Please wait {}"
# save_url_to_dir = functools.partial(save_url_file, msg=msg)
#
# url = 'http://mobilo24.eu/spis'
# file = 'spis.html'
# print(save_url_to_dir(url=url, file=file))
#
# url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
# file = 'logo.png'
# print(save_url_to_dir(url=url, file=file))


'''optymalizacja funkcji przez cache'''

# import time
# import functools
#
# @functools.lru_cache()
# def Factorial(n):
#     time.sleep(0.1)
#     if n == 1:
#         return 1
#     else:
#         return n * Factorial(n - 1)
#
#
# start = time.time()
# for i in range(1, 11):
#     print("{}! = {}".format(i, Factorial(i)))
# stop = time.time()
# print("Czas", stop - start)
#
# print(Factorial.cache_info())


''''''
# import time
# import functools
# print("Przykład pierwszy")
#
#
# def fib(n):
#     if n <= 2:
#         result = n
#     else:
#         result = fib(n - 1) + fib(n - 2)
#
#     return result
#
#
# start = time.time()
# for x in range(1, 30):
#     print("{} = {} fib".format(x, fib(x)))
# end = time.time()
# print("Całkowity czas wykonywania działania to: {0:.2f} sek", end - start)
# print("Przykład drugi")
#
#
# @functools.lru_cache()
# def fib(n):
#     if n <= 2:
#         result = n
#     else:
#         result = fib(n - 1) + fib(n - 2)
#
#     return result
#
#
# start = time.time()
# for x in range(1, 30):
#     print("{} = {} fib".format(x, fib(x)))
# end = time.time()
# print("Całkowity czas wykonywania działania to: ", end - start)
# print(fib.cache_info())


'''wyrażenie lambda'''


# def duble(x):
#     return x * 2
#
#
# print(duble(2))
#
# y = lambda x: x*2
# print(y(2))
#
#
# def potega(x, y):
#     return x ** y
#
#
# print(potega(4, 6))
#
# a = lambda x, y: x ** y
# print(a(4, 6))


# def czy_parzysta(x):
#     return x % 2 == 0
#
#
# lista = [1, 2, 8, 5, 30, 64, 83, 44, 278, 19, 28, 31, 9]
# print("Parzyste")
# filtrowanie_parzystych = list(filter(czy_parzysta, lista))
# print(filtrowanie_parzystych)
#
# print("Nieparzyste")
# print(list(filter(lambda x: x % 2 != 0, lista)))

''''''

text_list = ['x', 'xxx', 'xxxxx', 'xxxxxxx', '']

dlugosc_napisu = lambda x: len(x)
print(dlugosc_napisu("domek"))
print(list(map(dlugosc_napisu, text_list)))
print(list(map(lambda x: len(x), text_list)))



