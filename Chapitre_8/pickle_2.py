#!/usr/bin/env python3
import pickle


def main():
    fichier = "bdd/pickle.db"
    print(f"Lecture de '{fichier}'...")
    with open(fichier, "rb") as f:
        obj = pickle.load(f)
    print("Type de l'objet: {}".format(type(obj)))
    print(f"__str__ sur l'objet: {obj}".format(obj))


if __name__ == "__main__":
    main()
