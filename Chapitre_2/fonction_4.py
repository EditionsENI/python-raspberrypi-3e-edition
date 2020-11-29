#!/usr/bin/env python3


def args_nommes(arg1="", arg2=0, arg3=None):
    print(f"Argument arg1: {arg1}")
    print(f"Argument arg2: {arg2}")
    print(f"Argument arg3: {arg3}")


if __name__ == "__main__":
    args = {
        "arg1": "Bonjour!",
        "arg2": 150,
        "arg3": 3000
    }
    args_nommes(**args)
