#!/usr/bin/env python3


class Voiture:
    def __init__(self, annee=0):
        self.annee = annee

    def __str__(self):
        return "Je suis une voiture de l'année {self.annee}."


class Peugeot(Voiture):
    def __init__(self, annee, slogan):
        super().__init__(annee)
        self.slogan = slogan

    def __str__(self):
        return super().__str__() + \
            " Je suis de marque Peugeot." + \
            f" Mon slogan: {self.slogan}"


if __name__ == "__main__":
    v1 = Voiture(annee=2000)
    print(v1)
    v2 = Peugeot(annee=2002, slogan="Passion for life.")
    print(v2)
