def dodawanie(liczby):
    suma = 0
    for znaki in liczby:
        suma += znaki
    return suma


def mnozenie(liczby):
    iloczyn = 1
    for znaki in liczby:
        iloczyn *= znaki
    return iloczyn