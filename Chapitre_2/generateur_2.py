#!/usr/bin/env python3


def fois_deux(ma_liste):
    liste = []
    for element in ma_liste:
        yield element * 2


if __name__ == "__main__":
    liste = [5, 10, 50, 100]
    print(f"Avant fois_deux(): {liste}")
    ngen = fois_deux(liste)
    print(f"Générateur: {ngen}")
    print("Élement: {0}".format(next(ngen)))
    print("Élement: {0}".format(next(ngen)))
    print("Élement: {0}".format(next(ngen)))
    print("Élement: {0}".format(next(ngen)))
    print("Élement: {0}".format(next(ngen)))
