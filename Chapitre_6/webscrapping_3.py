#!/usr/bin/env python3
from html.parser import HTMLParser
import threading
import requests
import re
import os

url = "https://fr.wikipedia.org/wiki/France"
repertoire = "./images"


class ParseurHTML(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            tagattrs = dict((x, y) for x, y in attrs)
            img = tagattrs["src"]
            if re.search(r"upload", img):
                image_info = (f"https:{img}", os.path.basename(img))
                threading.Thread(
                    target=lambda: sauvegarder_image(image_info)
                ).start()


def sauvegarder_image(image_info):
    image_url, image_chemin = image_info
    with requests.Session() as session:
        image = session.get(image_url)
        with open(f"images/{image_chemin}", "wb") as sortie:
            print(f"Sauvegarde de {image_chemin} ...")
            sortie.write(image.content)


def main():
    if not os.path.exists(repertoire):
        os.mkdir(repertoire)

    parseur = ParseurHTML()
    with requests.Session() as session:
        reponse = session.get(url)
        page = reponse.text
        parseur.feed(page)


if __name__ == "__main__":
    main()
