#!/usr/bin/env python3


class Voiture:
    def __init__(self, marque="", annee=0):
        self.marque = marque
        self.annee = annee
        print(self)

    def __str__(self):
        return f"Je suis une voiture:\n{self.marque}\n{self.annee}"


class Marque:
    def __init__(self, nom=""):
        self.nom = nom

    def __str__(self):
        if self.nom == "Peugeot":
            slogan = "La marque au lion"
        elif self.nom == "Renault":
            slogan = "Passion for life"
        else:
            slogan = "Aucun"
        return f"{self.nom}: {slogan}"


class Annee:
    def __init__(self, annee=0):
        self.annee = annee

    def __str__(self):
        return f"Annee: {self.annee}"


if __name__ == "__main__":
    v1 = Voiture(marque=Marque("Peugeot"), annee=Annee(1999))
    v2 = Voiture(marque=Marque("Renault"), annee=Annee(2009))
