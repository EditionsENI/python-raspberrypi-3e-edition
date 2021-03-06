#!/usr/bin/env python3
from PIL import ImageDraw
from PIL import Image


def main():
    img = Image.new("RGB", size=(200, 200), color="green")
    draw = ImageDraw.Draw(img)
    draw.ellipse((50, 50, 150, 150), fill="red")
    img.save("images/cercle.png")


if __name__ == "__main__":
    main()
