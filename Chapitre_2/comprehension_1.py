#!/usr/bin/env python3


def main():
    ma_liste = list(range(1, 11))
    mon_tri = []

    for i in ma_liste:
        if i % 2 == 0:
            mon_tri.append(i)

    print(mon_tri)


if __name__ == "__main__":
    main()
