'''OPERATORY PRZECIĄŻANIA'''

# class Clock:
#     def __init__(self, hour=0, minutes=0, seconds=0):
#         self.hour = hour
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def editTime(self, hour=0, minutes=0, seconds=0):
#         if self.seconds + seconds >= 60:
#             self.minutes += (self.seconds + seconds) // 60
#             self.seconds = (self.seconds + seconds) % 60
#         else:
#             self.seconds += seconds
#
#         if self.minutes + minutes >= 60:
#             self.hour += (self.minutes + minutes) // 60
#             self.minutes = (self.minutes + minutes) % 60
#         else:
#             self.minutes += minutes
#
#         if self.hour + hour >= 24:
#             if self.hour + hour == 24:
#                 self.hour = 0
#             elif self.hour + hour > 24:
#                 self.hour = (self.hour + hour) % 24
#             else:
#                 self.hour += hour
#
#     def __str__(self):
#         return f"Czas to {self.hour}:{self.minutes}:{self.seconds}"
#
#     def __eq__(self, other):
#         return self.hour == other.hour and self.minutes == other.minutes and self.seconds == other.seconds
#
#     def __add__(self, other):
#         zegarek = Clock(self.hour, self.minutes, self.seconds)
#         zegarek.editTime(other.hour, other.minutes, other.seconds)
#         return zegarek
#
#
# zegarek = Clock(5, 45, 12)
# zegarekA = Clock(5, 45, 12)
# zegarek.editTime(18, 20, 10)
# print(zegarek)
# zegarekB = zegarek + zegarekA
# print(zegarekB)
#
# clock_one = Clock(23, 0, 0)
# clock_two = Clock(3, 0, 0)
#
# print("hours counting test")
# print(clock_one + clock_two)
# print(clock_two == clock_one)
#
'''ZAPISYWANIE OBIEKTU DO PLIKU'''
#
# import _pickle as pick
# file = open("//temp/ćwiczenia/pl.txt", "wb")
# pick.dump(zegarek, file)
# file.close()
#
# print("ODCZYT")
# filr_pick = open("/temp/ćwiczenia/pl.txt", "rb")
# zegarek = pick.load(filr_pick)
# filr_pick.close()
# print(zegarek)
