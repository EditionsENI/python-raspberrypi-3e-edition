#!/usr/bin/env python3
import shelve


def main():
    fichier = "bdd/shelve.db"
    print(f"Lecture de '{fichier}'...")
    bdd = shelve.open(fichier)
    print("Objets stockés: Clé => Valeur")
    for cle, valeur in bdd.items():
        print(f"[{cle}] => [{valeur}]")
    print(bdd["str"])
    bdd.close()


if __name__ == "__main__":
    main()
