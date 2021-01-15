#!/usr/bin/env python3
import sys


def main():
    for numero, arg in enumerate(sys.argv):
        print(f"Argument#{numero}: {arg}")


if __name__ == "__main__":
    main()
