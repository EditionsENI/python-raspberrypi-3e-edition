#!/usr/bin/env python3
import os
import sys


def format_commande(utilisateur, choix):
    commande
    if choix == "a":
        commande = f"/usr/sbin/useradd -m {utilisateur}"
    elif choix == "s":
        commande = f"/usr/sbin/userdel -r {utilisateur}"
    return commande


def main():
    uid = os.getuid()

    if uid != 0:
        sys.exit("Vous devez être administrateur pour lancer ce script!")

    choix = input(
        "Souhaitez-vous ajouter/supprimer un utilisateur ? [a/s] ").strip()

    if choix not in ("a", "s"):
        sys.exit("Réponse non comprise !")

    utilisateur = input("Tapez l'utilisateur à ajouter: ").strip()
    commande = format_commande(utilisateur, choix)
    retour = os.system(commande)

    if retour != 0:
        print("Probleme d'execution du script!")

    sys.exit(retour)


if __name__ == "__main__":
    main()
