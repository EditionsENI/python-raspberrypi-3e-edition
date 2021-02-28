#!/usr/bin/env python3
import pudb


def explosion(arg="kaboom!", elem=1):
    pudb.set_trace()
    elem = elem + 1
    return elem / 0


def main():
    for i in range(5):
        if i == 3:
            explosion(elem=i)


if __name__ == "__main__":
    main()
