#!/usr/bin/env python3
import pwd
import sys


def main():
    utilisateur = input("Tapez l'utilisateur à rechercher: ")
    infos = None

    try:
        infos = pwd.getpwnam(utilisateur)
    except KeyError:
        print(f"L'utilisateur '{utilisateur}' n'existe pas sur ce système!")
        sys.exit(1)

    print("Nom d'utilisateur:", infos.pw_name)
    print("Mot de passe     :", infos.pw_passwd)
    print("Commentaire      :", infos.pw_gecos)
    print("UID/GID          :", infos.pw_uid, "/", infos.pw_gid)
    print("Répertoire perso :", infos.pw_dir)
    print("Shell par défaut :", infos.pw_shell)


if __name__ == "__main__":
    main()
