#!/usr/bin/env python3
import csv
from csv_1 import generer_donnees


def enregistrer_dialecte():
    csv.register_dialect("pourcent", delimiter="%")


def main():
    enregistrer_dialecte()
    fichier = "bdd/dialecte.csv"
    print(f"Ecriture dans le fichier '{fichier}'...")
    with open(fichier, "w") as f:
        writer = csv.writer(f, dialect="pourcent")
        for ligne in generer_donnees():
            writer.writerow(ligne)
    print("OK!")


if __name__ == "__main__":
    main()
