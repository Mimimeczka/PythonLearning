# id = {"nitka" : "igla", "waz" : "rzeczny", "dupa" : "wolowa"}
# login = input("LOGIN: ")
# haslo = input("HASLO: ")
# if login in id.keys() and haslo == id[login]:
#     print("zalogowany\\a")
# else:
#     print("wypierdalaj nie masz dostepu")




# '''INSTRUKCJA WARUNKOWA = służy by pewna częśc kodu została wykonana wtedy i tylko wtedy'''
# i = 3
# if i > 0:
#     print(i)

# for i in range(1, 100):
#     if i % 17 == 0:
#         if i % 2 == 0:
#             print("liczba %d jest podzielna zarówno przez 17 jak i jest parzysta" %(i))
#         print("liczba  %d jest podzielna przez 17" %(i))

# for x in range(0, 11):
#     for y in range(0, 11):
#         if x * y < 100:
#             print(" ", end="")
#         if x * y < 10:
#             print(" ", end="")
#         print(" " + str(x * y), end="")
#     print("")

# for x in range(0, 11):
#     for y in range(0, 11):
#         print(" [:3]".format(y * y), end="")
#     print("")