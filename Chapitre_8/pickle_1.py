#!/usr/bin/env python3
import pickle
from klasse import MaClasse


def main():
    fichier = "bdd/pickle.db"
    print(f"Ecriture dans '{fichier}'...")
    with open(fichier, "wb") as f:
        maClasse = MaClasse(150)
        pickle.dump(maClasse, f)
    print("OK!")


if __name__ == "__main__":
    main()
