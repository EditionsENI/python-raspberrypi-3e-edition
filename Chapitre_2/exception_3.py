#!/usr/bin/env python3


def main():
    fichier = "pasla.txt"
    print(f"J'essaye d'ouvrir '{fichier}' ...")

    try:
        open(fichier)
    except (FileNotFoundError, OSError) as e:
        print("Le fichier n'existe pas!")
        print("ou il y a eut une erreur système!")
        print(f"Nom de l'exception: {e}")
    except Exception:
        print("Une exception s'est produite!")


if __name__ == "__main__":
    main()
