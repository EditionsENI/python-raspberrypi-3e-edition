#!/usr/bin/env python3
import os


def main():
    fichier = "monfichier.txt"

    f = open(fichier, "w")
    f.write("J'écris une ligne dans le fichier.\n")
    f.write("Puis une autre.\n")
    f.close()

    f = open(fichier, "r")
    for line in f:
        print(line.strip())
    f.close()

    os.unlink(fichier)


if __name__ == "__main__":
    main()
