# '''KOLKO I KRZYZYK w sposob obiektowy'''
#
# class Board:
#     def __init__(self, player):
#         self.board = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
#         self.player = player
#         self.win = False
#
#     def checkInWin(self):
#         # ta funkcja jest odpowiedzalna za sprawdzenie wygranej
#         for x in range(0, 3):
#             if self.board[x][0] == self.board[x][1] and self.board[x][1] == self.board[x][2] and (self.board[x][2] == "o" or self.board[x][2] == "x"):
#                 self.win = True
#                 return True
#         for y in range(0, 3):
#             if self.board[0][y] == self.board[1][y] and self.board[1][y] == self.board[2][y] and (self.board[2][y] == "o" or self.board[2][y] == "x"):
#                 self.win = True
#                 return True
#         if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and (self.board[2][2] == "o" or self.board[2][2] == "x"):
#             self.win = True
#             return True
#         if self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2] and (self.board[2][0] == "o" or self.board[2][0] == "x"):
#             self.win = True
#             return True
#         return False
#
#     def checkIfDraw(self):
#         # ta funkcja informuje o remisie
#         if not self.checkInWin():
#             for wiersz in self.board:
#                 for element in wiersz:
#                     if element == "*":
#                         return False
#             return True
#         else:
#             return False
#
#     def printTheBoard(self):
#         # ta funkcja jest odpowiedzialna za wyświetlenie planszy
#         print("  1 2 3")
#         numer_wiersza = 1
#         for wiersz in self.board:
#             print(numer_wiersza, end=" ")
#             for element in wiersz:
#                 print(element, end=" ")
#             print()
#             numer_wiersza += 1
#
#     def checkIfFree(self, x, y):
#         return self.board[x - 1][y - 1] == "*"
#
#     def changeThePlayer(self):
#         if self.player == "o":
#             self.player = "x"
#         else:
#             self.player = "o"
#
#     def PutToBoard(self, x, y):
#         if self.checkIfFree(x, y):
#             self.board[x - 1][y - 1] = self.player
#             self.changeThePlayer()
#
#     def getPlayer(self):
#         return self.player
#
#     def returnBoard(self):
#         return self.board
#
#
#
# player = input("Napisz 'x' jeśli pierwszy zaczyna a jesli nie to napisz 'o' ")
#
# board = Board(player)
#
# while not board.checkInWin() and not board.checkIfDraw():
#     board.printTheBoard()
#     x, y = [int(x) for x in input("podaj wspolrzedne pola w ktorym chcesz postawic znak: ").split()]
#     board.PutToBoard(x, y)
#
# board.printTheBoard()
#
# '''informacja o wygranej'''
# if board.checkInWin():
#     if board.getPlayer() == "x":
#         print("wygrywa 'o' gratulujemy!!!")
#     else:
#         print("wygrywa 'x' gratulujemy!!!")
# else:
#     print("nastapil remis")










# '''GRA KÓŁKO I KRZYŻYK'''
# def wyswietl_plansze(mapa2D):
#     # ta funkcja jest odpowiedzialna za wyświetlenie planszy
#     print("  1 2 3")
#     numer_wiersza = 1
#     for wiersz in mapa2D:
#         print(numer_wiersza, end=" ")
#         for element in wiersz:
#             print(element, end=" ")
#         print()
#         numer_wiersza += 1
#
#
# def wygrana(mapa2D):
#     # ta funkcja jest odpowiedzalna za sprawdzenie wygranej
#     for x in range(0, 3):
#         if mapa2D[x][0] == mapa2D[x][1] and mapa2D[x][1] == mapa2D[x][2] and (mapa2D[x][2] == "o" or mapa2D[x][2] == "x"):
#             return True
#     for y in range(0, 3):
#         if mapa2D[0][y] == mapa2D[1][y] and mapa2D[1][y] == mapa2D[2][y] and (mapa2D[2][y] == "o" or mapa2D[2][y] == "x"):
#             return True
#     if mapa2D[0][0] == mapa2D[1][1] and mapa2D[1][1] == mapa2D[2][2] and (mapa2D[2][2] == "o" or mapa2D[2][2] == "x"):
#         return True
#     if mapa2D[2][0] == mapa2D[1][1] and mapa2D[1][1] == mapa2D[0][2] and (mapa2D[2][0] == "o" or mapa2D[2][0] == "x"):
#         return True
#     return False
#
#
# def remis(mapa2D):
#     # ta funkcja informuje o remisie
#     if not wygrana(mapa2D):
#         for wiersz in mapa2D:
#             for element in wiersz:
#                 if element == "*":
#                     return False
#         return True
#     else:
#         return False
#
# '''określenie kto zaczyna grac wcześniej'''
# graKrzyzyk = False
# pierwszy = input("Napisz 'x' jeśli pierwszy zaczyna a jesli nie to napisz 'o' ")
# if pierwszy == "x":
#     graKrzyzyk = True
#
# plansza = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
# # wyswietl_plansze(plansza)
#
# '''GRA - przebieg'''
# while (not remis(plansza)) and (not wygrana(plansza)):
#     wyswietl_plansze(plansza)
#     x, y = [int(x) for x in input("podaj wspolzedne pola w ktorym chcesz postawic znak: "). split()]
#     if plansza[x - 1][y - 1] == "*":
#         if graKrzyzyk:
#             plansza[x - 1][y - 1] = "x"
#             graKrzyzyk = False
#         else:
#             plansza[x - 1][y - 1] = "o"
#             graKrzyzyk = True
#
# '''informacja o wygranej'''
# wyswietl_plansze(plansza)
# if wygrana(plansza):
#     if graKrzyzyk:
#         print("wygrywa 'o' gratulujemy!!!")
#     else:
#         print("wygrywa 'x' gratulujemy!!!")
# else:
#     print("nastapil remis")
