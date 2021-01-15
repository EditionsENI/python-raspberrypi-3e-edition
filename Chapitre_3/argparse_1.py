#!/usr/bin/env python3
import argparse


def main():
    version = """%(prog)s 0.1"""
    description = """Démonstration du module argparse."""

    parseur = argparse.ArgumentParser(description=description)

    parseur.add_argument("--version",
                         action="version",
                         version=version)
    parseur.add_argument("-n", "--nom",
                         dest="nom",
                         default="Python",
                         help="nom par défaut",
                         type=str)
    parseur.add_argument("-a", "--age",
                         dest="age",
                         default="25",
                         help="age par défaut",
                         type=int)
    parseur.add_argument("-v", "--verbeux",
                         dest="verbeux",
                         default=False,
                         help="verbosité du script",
                         action="store_true")
    parseur.add_argument(dest="restant",
                         help="arguments restants",
                         nargs="*")

    args = parseur.parse_args()

    print("Nom?       :", args.nom)
    print("Age?       :", args.age)
    print("Verbeux?   :", args.verbeux)
    print("Arguments? :", args.restant)


if __name__ == "__main__":
    main()
