#!/usr/bin/env python3
class CrashException(BaseException):
    pass


def main():
   try:
       print("Je veux voler!")
       raise CrashException("Mayday!")
   except CrashException as crash:
       print(".. mais l'Homme ne vole pas.")
       print(f"Attention! {crash}")
   finally:
       print("Atterissage...")


if __name__ == "__main__":
    main()
