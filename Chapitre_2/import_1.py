#!/usr/bin/env python3
import os


def my_random():
    import random
    print("Voici un nombre généré au hasard:")
    print(random.random())


if __name__ == "__main__":
    if os.path.exists("/etc"):
        print("/etc existe!")
    my_random()
    print(f"Le module os? {os}")
    print(f"Le module random? {random}")
