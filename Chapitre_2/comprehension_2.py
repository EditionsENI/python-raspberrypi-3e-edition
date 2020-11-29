#!/usr/bin/env python3


def main():
    mon_tuple = tuple(i for i in range(1, 11) if i % 2 == 0)
    print(f"Avec un tuple: {mon_tuple}")
    mon_tuple = list(i for i in range(1, 11) if i % 2 == 0)
    print(f"Avec une liste: {mon_tuple}")
    mon_dict = {x: x**x for x in range(0, 5)}
    print(f"Avec un dictionnaire: {mon_dict}")
    mon_set = set(i for i in range(1, 11) if i % 2 == 0)
    print(f"Avec un set: {mon_set}")


if __name__ == "__main__":
    main()
