#!/usr/bin/env python3


def args_nommes(arg1="", arg2=0, arg3=None):
    print(f"Argument arg1: \"{arg1}\"")
    print(f"Argument arg2: {arg2}")
    print(f"Argument arg3: {arg3}")


if __name__ == "__main__":
    args_nommes()
    args_nommes("", 2, 3)
    args_nommes(arg3=0, arg1="hi!", arg2=150)
