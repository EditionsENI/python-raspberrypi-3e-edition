#!/usr/bin/env python3
import os


def main():
    fichier = "monfichier.txt"
    with open(fichier, "w") as f:
        f.write("J'écris une ligne dans le fichier.\n")
        f.write("Puis une autre.\n")
    with open(fichier, "r") as f:
        for line in f:
            print(line.strip())
    os.unlink(fichier)


if __name__ == "__main__":
    main()
