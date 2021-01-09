#!/usr/bin/env python3
import sys


def main():
    for numero, arg in enumerate(sys.argv):
        print('Argument#{0}: {1}'.format(numero, arg))


if __name__ == "__main__":
    main()
