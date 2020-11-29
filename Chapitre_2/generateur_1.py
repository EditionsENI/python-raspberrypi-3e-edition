#!/usr/bin/env python3


def fois_deux(ma_liste):
    liste = []
    for element in ma_liste:
        liste.append(element * 2)
    return liste


if __name__ == "__main__":
    liste = [5, 10, 50, 100]
    print(f"Avant fois_deux(): {liste}".format(liste))
    nliste = fois_deux(liste)
    print(f"Apres fois_deux(): {nliste}".format(nliste))
