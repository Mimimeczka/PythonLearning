''' Funkcje i wartości domyślne argumentów'''
# def show_progress(how_many:int, character = "*"):
#     line = character * how_many
#     print(line)
# show_progress(10)
# show_progress(15)
# show_progress(30)
# show_progress(10, '-')
# show_progress(15, '+')

'''Specjalne argumenty - args i kwargs'''
# def calculate_paint(efficency_ltr_per_m2, *rooms):
#     total_area = sum(rooms)
#     paint = total_area * efficency_ltr_per_m2
#     return paint
#
# print(calculate_paint(0.25, 42, 28, 30))
#
# rooms = [42, 28, 30]
# print(calculate_paint(0.25, *rooms))

''''''

# plik = "og_it.txt"
# def log_it(*args):
#     with open("og_it.txt", "a") as file:
#         for arg in args:
#             file.write(arg + ' ')
#         file.write("\n")
#
# # log_it('Starting processing forecasting')
# # log_it('ERROR', 'Not enough data', 'invoices', '2020')
#
# def read_file():
#     with open("og_it.txt", "r") as file:
#         for line in file:
#             print(line)
#
# read_file()

'''funkcja jako zmienna'''
# def start(*args):
#     print("Zaczynam jechać z: ", *args)
#
# def prosto(*args):
#     print("Jade prosto z: ", *args)
#
# def lewo(*args):
#     print("Skręcam w lewo z: ", *args)
#
# def prawo(*args):
#     print("Skręcam w prawo z: ", *args)
#
# def cofa(*args):
#     print("Cofam sie z: ", *args)
#
# def koniec(*args):
#     print("Koniec trasy z: ", *args)
#
# trasa = [start, prawo, prosto, lewo, lewo, prosto, cofa, prosto, lewo, koniec]
#
# danie = "pizza"
#
# for polecenie in trasa:
#     polecenie(danie)

''''''


# def double(x):
#     return 2 * x
#
#
# def root(x):
#     return x ** 2
#
#
# def negative(x):
#     return -x
#
#
# def div2(x):
#     return x / 2
#
#
# number = 8
# transformations = [double, root, div2, negative]
# transformations_2 = [root, root, div2, double]
# tmp_return_value = number
#
# for position in transformations_2:
#     print(position(tmp_return_value))

'''funkcja jako argument funkcji'''
# def dodaj(*agrs):
#     print("Dodano: ", *agrs)
#
# def mieszaj(*agrs):
#     print("Mieszanie: ", *agrs)
#
# def gotuj(*args):
#     print("Gotowanie: ", *args)
#
# def polecenia(czynnosc, *skladniki):
#     czynnosc(*skladniki)
#
# gotowanie = [(dodaj, "mleko"), (dodaj, "jajka"), (dodaj, "maka"), (mieszaj, "wszystko"), (gotuj, "wszystko")]
#
# for czynnosc, skladnik in gotowanie:
#     polecenia(czynnosc, skladnik)

''''''


# def double(x):
#     return 2 * x
#
#
# def root(x):
#     return x ** 2
#
#
# def negative(x):
#     return -x
#
#
# def div2(x):
#     return x / 2
#
#
# def generate_values(function, *args):
#     results = []
#     for arg in args:
#         results.append(function(arg))
#     return results
#
#
# x_table = list(range(11))
#
# print(generate_values(double, *x_table))
# print(generate_values(root, *x_table))
# print(generate_values(negative, *x_table))
# print(generate_values(div2, *x_table))

'''funkcje zwracające funkcje'''

# def CreateFunction(kind = "+"):
#     source = '''
# def f(*args):
#     result = 0
#     for x in args:
#         result {}= x
#     return result'''. format(kind)
#     exec(source, globals())
#     return f
#
# f_add = CreateFunction("+")
# print(f_add(1, 2, 3))
# f_subs = CreateFunction("-")
# print(f_subs(1, 2, 3))

''''''

from datetime import datetime


def create_function(span):
    if span == "m":
        sek = 60
    elif span == "h":
        sek = 360
    else:
        sek = 86400
    source = '''
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]
    '''.format(sek)
    exec(source, globals())
    return f


start = datetime(2019, 1, 1, 0, 0, 0)
end = datetime.now()

time_m = create_function("m")
print(time_m(start, end))
time_h = create_function("h")
print(time_h(start, end))
time_d = create_function("d")
print(time_d(start, end))


