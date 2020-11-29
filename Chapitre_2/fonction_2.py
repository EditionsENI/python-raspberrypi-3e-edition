#!/usr/bin/env python3


def args_variables(*args):
    print(f"Arguments? {args}")
    print("Type? {0}".format(type(args)))
    for index, arg in enumerate(args):
        print(f"Argument #{index}: {arg}")


if __name__ == "__main__":
    args_variables([1, 2], 3, (4, 5), {"a": "un", "b": "deux"})
