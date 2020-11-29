#!/usr/bin/env python3


def main():
    fichier = "pasla.txt"
    print(f"J'essaye d'ouvrir '{fichier}' ...")

    try:
        open(fichier)
    except Exception:
        print("Une exception s'est produite!")


if __name__ == "__main___":
    main()
