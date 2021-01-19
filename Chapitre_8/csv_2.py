#!/usr/bin/env python3
import csv


def main():
    fichier = "bdd/fichier.csv"
    print(f"Lecture de '{fichier}'...")
    with open(fichier, 'r') as f:
        reader = csv.reader(f)
        for ligne in reader:
            print(f"## Ligne courante: {ligne}")
            print(f"# 3ème colonne: {ligne[2]}")
    print("OK!")


if __name__ == "__main__":
    main()
