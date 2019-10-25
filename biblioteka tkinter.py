# import tkinter

'''LABELKA'''
# window = tkinter.Tk()
# window.title("Pierwsze okno")
# window.geometry("400x400+200+200")
# myLabel = tkinter.Label(window, text="Jakis napis", fg="red", bg="pink", width=50, font=("Arial", 20), anchor="s")
# myLabel.pack()
# myLabel.place(relx=0, rely=0.45)
# window.mainloop()

'''PRZYCISK'''
# window = tkinter.Tk()
# window.title("Tworzenie przycisku")
#
# def buttonClicked():
#     labelka = tkinter.Label(window, text="nowa labelka", fg="red")
#     labelka.pack()
#
# frame = tkinter.Frame(window, width=80, height=40, bg="red")
# frame.pack_propagate(0)
# frame.pack()
#
# button = tkinter.Button(frame, text="ok", command=buttonClicked, fg="red", bg="white")
# button.pack(fill="both", expand=1, padx=10, pady=2)
# tkinter.mainloop()

'''LICZENIE RÓŻNICY SILNIA'''
# def factorial(n):
# # ta funkcja jest odpowiedzialna za liczenie silni
#     liczenie = 1
#     for x in range(1, n + 1):
#         liczenie *= x
#     return liczenie
#
#
# window = tkinter.Tk()
# window.title("Różnica silni")
#
# def closeWindow():
# # ta funkcja jest odpowiedzialna za zamknięcie formatki
#     window.destroy()
#
# labelka = tkinter.Label(window, text="Podaj dwie liczby oddzielone spacja").pack(side=tkinter.TOP, padx=10, pady=10)
#
# entry = tkinter.Entry(window, width=10)
# entry.pack(side=tkinter.TOP, padx=10, pady=10)
#
# odpowiedz = tkinter.Label(window, text="Odpowiedz: ")
# odpowiedz.pack(side=tkinter.TOP, padx=10, pady=10)
#
# def getValues():
# # ta funkcja jest odpowiedzialna za liczenie różnicy z dwuch silni
#     x, y = [int(x) for x in entry.get().split(" ")]
#     wynik = (factorial(x) - factorial(y))
#     print(wynik)
#     odpowiedz["text"] = "Odpowiedz:" + str(wynik)
#
# b_a = tkinter.Button(window, text="ok", command=getValues).pack(side=tkinter.LEFT)
#
# b_B = tkinter.Button(window, text="close", command=closeWindow).pack(side=tkinter.RIGHT)
#
# window.mainloop()

'''PROBLEM OSMIU HETTMANÓW'''
import tkinter
import itertools
from tkinter import ttk

def attack(list2d, n):
# ta funkcja sprawdza czy hetmany sie atakują
    for raw in list2d:
        for i in range(1,n):
            if [raw[0] + i, raw[1] + i] in list2d:
                return True
            if [raw[0] + i, raw[1] - i] in list2d:
                return True
            if [raw[0] - i, raw[1] - i] in list2d:
                return True
            if [raw[0] - i, raw[1] + i] in list2d:
                return True
    return False


def NumberOfQueens(n):
# ta funkcja odpowiada na pytanie ile jest hetmanów na szachownicy
    coordinatea = [x for x in range(n)]
    permutations = [list(x) for x in itertools.permutations(coordinatea)]
    # print(permutations)
    answer = 0
    for combination in permutations:
        Queens2DList = [[i, combination[i]] for i in range(n)]
        if not attack(Queens2DList,n):
            answer += 1
    return answer

window = tkinter.Tk()
window.title("Problem n hetmanów")

def closeWindow():
# ta funkcja jest odpowiedzialna za zamknięcie formatki
    window.destroy()

labelka = ttk.Label(window, text="Podaj liczbe naturalną oznaczającą wymiar szachownicy").pack(side=tkinter.TOP, padx=10, pady=10)

entry = ttk.Entry(window, width=10)
entry.pack(side=tkinter.TOP, padx=10, pady=10)

odpowiedz = ttk.Label(window, text="Odpowiedz: ")
odpowiedz.pack(side=tkinter.TOP, padx=10, pady=10)

def getValues():
    '''ta funkcja jest odpowiedzialna za liczenie różnicy z dwuch silni'''
    n = int(entry.get())
    wynik = NumberOfQueens(n)
    print(wynik)
    odpowiedz["text"] = "Odpowiedz:" + str(wynik)

b_a = ttk.Button(window, text="ok", command=getValues).pack(side=tkinter.LEFT)

b_B = ttk.Button(window, text="close", command=closeWindow).pack(side=tkinter.RIGHT)

window.mainloop()


