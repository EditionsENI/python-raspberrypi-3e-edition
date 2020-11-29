#!/usr/bin/env python3


def iter_demo():
    ma_liste = [1, 2, 3, 4, 5]
    print(f"Ma liste: {ma_liste}")
    mon_iter = ma_liste.__iter__()
    print(f"Mon iterateur: {mon_iter}")
    print("Éléments:")
    print(next(mon_iter))
    print(next(mon_iter))
    print(next(mon_iter))
    print(next(mon_iter))
    print(next(mon_iter))
    print(next(mon_iter))


if __name__ == "__main__":
    iter_demo()
