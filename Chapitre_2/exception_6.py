#!/usr/bin/env python3


def main():
    try:
        print("Je divise 1 / 0 ...")
        x = 1 / 1
    except ZeroDivisionError:
        print("Erreur!")
    finally:
        print("finally est toujours exécuté.")


if __name__ == "__main__":
    main()
