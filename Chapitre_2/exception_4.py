#!/usr/bin/env python3


def main():
   ma_liste = [1, 2, 3]
   indice = 2

   try:
       ma_valeur = ma_liste[indice]
   except IndexError:
       print("Cet indice n'est pas disponible!")
   else:
       print(f"Valeur à l'indice {indice}: {ma_valeur}")


if __name__ == "__main__":
    main()
