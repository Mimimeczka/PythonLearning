'''generator'''
# import datetime as dt
#
# def Foo(year, month, day, maxday):
#     data = dt.datetime(year, month, day)
#
#     for i in range(maxday):
#         yield(data + dt.timedelta(days=i))
#
#
# for x in Foo(2000, 1, 1, 5):
#     print(x)

''''''

# def Combinations(products, promotions, customers):
#     for product in products:
#         for promotion in promotions:
#             for customer in customers:
#                 yield"{} - {} -{}".format(product, promotion, customer)
#
#
# products = ["Product {}".format(i) for i in range(1, 4)]
# promotions = ["Promotion {}".format(i) for i in range(1, 3)]
# customers = ['Customer {}'.format(i) for i in range(1, 5)]
#
# combinations = Combinations(products, promotions, customers)
#
# for c in combinations:
#     print(c)

'''Przykład generatora strumień danych'''

# file = open("generator_strumien_danych.txt")
# records = []
# for line in file:
#     if ":" in line:
#         type, action = line.rstrip("\n").split(":")
#         record = (type, action)
#         records.append(record)
# file.close()
# print(records)

''''''
# def get_records(filePath):
#     print("---OPENING FILE---")
#     file = open(filePath)
#     for line in file:
#         if ":" in line:
#             type, action = line.rstrip("\n").split(":")
#             record = (type, action)
#             yield record
#     print("---OPENING FILE---")
#     file.close()
#
# for record in get_records("generator_strumien_danych.txt"):
#     print("Type: {} is: {}".format(record[0], record[1]))


''''''

# import random
#
# def random_with_sum(number_of_values, asserted_sum):
#     trial = 0
#     numbers = list(range(number_of_values))
#     while True:
#         trial += 1
#         for i in range(number_of_values):
#             numbers[i] = random.randint(1, 101)
#
#         if sum(numbers) == asserted_sum:
#             yield ((trial, numbers))
#             trial = 0
#
#
# for i in range(10):
#     (number_of_trials, numbers) = next(random_with_sum(3, 100))
#     print(number_of_trials, numbers)


'''Przykład generetora funkcja grep'''
import os
path = "cwiczenia strony internetowe"
search_string = "waz"
file_extension = ".py"
for dir_name, subdirs, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(file_extension):
            fullFilename = (os.path.join(dir_name, filename))
            for line in open(fullFilename):
                if search_string in line:
                    print(filename)


''''''

import os
path = "/Users/justyna/Desktop/python/alx"
search_string = "file"
file_extension = ".py"

def generate_files(base_dir, file_extension):
    for dir_name, subdirs, filenames in os.walk(base_dir):
        for filename in filenames:
            if filename.endswith(file_extension):
                fullFilename = (os.path.join(dir_name, filename))
                yield fullFilename


def grep_files(searching_string, files):
    for file in files:
        with open(file) as text:
            if searching_string in text.read():
                yield file

file_generator = generate_files(path, file_extension)

for file in grep_files(search_string, file_generator):
    print(file)


''''''

import os
import requests

dir = "/Users/justyna/PycharmProjects/udemy/python dla średniozaawansowanych/cwiczenie strony internetowe"

def gen_get_files(dir):
    for d in os.listdir(dir):
        if os.path.isfile(d):
            yield os.path.join(dir, d)


def gen_get_file_lines(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            yield line.strip()


def check_webpage(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False


try:
    os.mkdir('/Users/justyna/PycharmProjects/udemy/python dla średniozaawansowanych/przyklady')
except:
    pass

with open('/Users/justyna/PycharmProjects/udemy/python dla średniozaawansowanych/przyklady/przykladA.py', 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')

with open('/Users/justyna/PycharmProjects/udemy/python dla średniozaawansowanych/przyklady/przykladb.py', 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')

for file in gen_get_files('/Users/justyna/PycharmProjects/udemy/python dla średniozaawansowanych/przyklady'):
    for line in gen_get_file_lines(file):
        print("{} - {} - {}".format(file, line, check_webpage(line)))


'''itertools'''
# import itertools as it
# lista = ["a", "b", "c", "d"]
#
# for combination in it.combinations_with_replacement(lista, 3):
#     print(combination)
#
# '''na ile możliwości można uzbierać 100zł w portwelu, bez powtarzania sie'''
# portfel = [20, 20, 20, 10, 10, 50, 100, 5, 5, 2, 1, 1, 1, 1, 1, 1, 1, 10]
# mozliwosci = set()
# for i in range(1, 101):
#     for setka in it.combinations(portfel, i):
#         if sum(setka) == 100:
#             mozliwosci.add(setka)
# print(mozliwosci)
# print(len(mozliwosci))
#
# '''na ile sposobów można wypłacić 100zł z możliwością powtarzania się banknotów'''
# portfel = [50, 20, 10]
# for i in range(1, 101):
#     for setka in it.combinations_with_replacement(portfel, i):
#         if sum(setka) == 100:
#             print(setka)
#
# ''''''
# import math
#
# notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
#
# for n in it.permutations(notes, 4):
#     print(n)
# print(math.factorial(len(notes))/math.factorial(len(notes) - 4))
#
# for n in it.combinations_with_replacement(notes, 4):
#     print(n)
# print(pow(len(notes), 4))

'''grupowanie danych'''
# import itertools as it
#
# data = []
#
# with open("/Users/justyna/PycharmProjects/udemy/python dla średniozaawansowanych/bledy.txt") as file:
#     for line in file:
#         if ":" in line:
#             n_line = line.rstrip("\n").split(":")
#             k_v = {"type": n_line[0], "action": n_line[1]}
#             data.append(k_v)
#
# print(data)
#
# data = sorted(data,  key=lambda x: x["type"])
#
# for key, elements in it.groupby(data, key=lambda x: x["type"]):
#     print("This key is {} and the group is {}". format(key, list(elements)))

''''''

# import os
# import itertools as it
#
# all_files = []
#
#
# def scantree(path):
#     return os.listdir(path)
#
#
# for x in scantree("/Users/justyna/PycharmProjects"):
#     path = os.path.join("/Users/justyna/PycharmProjects", x)
#     if os.path.isfile(path):
#         newfile = {"type": "file", "path": path}
#     else:
#         newfile = {"type": "dir", "path": path}
#     all_files.append(newfile)
#
# data = sorted(all_files,  key=lambda x: x["type"])
#
# for key, elements in it.groupby(data, key=lambda x: x["type"]):
#     print("This type is {} and the group is {}". format(key, list(elements)))

'''itertools przeglad'''

import itertools
import operator

# data = [1, 2, 4, 7, 4, 5, 9, 7]
# tydzien = ["Pon", "Wt", "Sr", "Czw", "Pt", "So", "Nd"]
# t_f = [True, False, True, False, True, False, True]
# kolory = ["dzwonek", "wino", "krajc", "czerwo"]
# figury = [9, 10, "J", "D", "K", "A"]
# do_st = [(1, 3), (5, 8), (9, 4)]
# czynnosci = ["nauka", "nauka", "nauka", "nauka", "nauka", "sprzatanie"]
#
# '''accumulate'''
# results = itertools.accumulate(data, operator.add)
#
# for result in results:
#     print(result)
#
# '''count'''
# for i in itertools.count(10, 3):
#     print(i)
#     if i >= 20:
#         break
#
# '''cycle'''
# for m in itertools.cycle(tydzien):
#     print(m)
#     if m == "Nd":
#         break
#
# '''chain'''
# result_chain = itertools.chain(data, tydzien)
# for r in result_chain:
#     print(r)
#
# '''compress'''
# result_compress = itertools.compress(tydzien, t_f)
# for r in result_compress:
#     print(r)
#
# '''dropwhile'''
# result_dropwhile = itertools.dropwhile(lambda x: x < 5, data)
# for r in result_dropwhile:
#     print(r)
#
# '''filterfalse'''
# resilt_filterfalse = itertools.filterfalse(lambda x: x % 2 == 0, data)
# for r in resilt_filterfalse:
#     print(r)
#
# '''islice'''
# result_islice = itertools.islice(tydzien, 2, 5)
# for r in result_islice:
#     print(r)
#
# '''product'''
# resilt_product = itertools.product(kolory, figury)
# for r in resilt_product:
#     print(r)
#
# '''repeat'''
# resilt_repeat = itertools.repeat("I <3 Eevee", 10)
# for r in resilt_repeat:
#     print(r)
#
# '''starmap'''
# resilt_starmap = itertools.starmap(operator.add, do_st)
# for r in resilt_starmap:
#     print(r)
#
# '''takewhile'''
# result_takepwhile = itertools.takewhile(lambda x: x < 5, data)
# for r in result_takepwhile:
#     print(r)
#
# '''tee'''
# tydzienA, tydzienB = itertools.tee(tydzien)
# for a in tydzienA:
#     print(a)
# for b in tydzienB:
#     print(b)
#
# '''zip_longest'''
# zipp = itertools.zip_longest(tydzien, czynnosci, fillvalue="nieznany")
# for z in zipp:
#     print(z)


def get_factors(x):
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list


candidate_list = list(range(1, 101))
filtered_list = list(itertools.filterfalse(lambda x: x != sum(get_factors(x)), candidate_list))

for p in filtered_list:
    print(p, get_factors(p))