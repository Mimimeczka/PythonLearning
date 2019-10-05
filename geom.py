import math


def GiveGeomSeqElement (a1 = 2, factor = 2, index = 2):
    # oblicza wartosc ciagu geometrycznego
    wzor = factor ** (index - 1) * a1
    return wzor


def GiveFactorForGeomSeq (termin, nexttermin):
    # wyznacza awrtosc wspolczynnika
    wynik = nexttermin / termin
    return wynik


def GiveSumOfNElementsGeomSeq (a1 = 2, factor = 2, n = 2):
    # wyznacza sume pierwszych wyrazow ciagu
    wzor = (a1 * (1 - factor **n)) / (1 - factor)
    return wzor
