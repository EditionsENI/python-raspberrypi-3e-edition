#!/usr/bin/env python3
from html.parser import HTMLParser
import requests
import re

url = "https://fr.wikipedia.org/wiki/France"


class ParseurWiki(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            tagattrs = dict((x, y) for x, y in attrs)
            img = tagattrs["src"]
            if re.search(r"upload", img):
                print("https:" + img)


def main():
    with requests.Session() as session:
        reponse = session.get(url)
        page = reponse.text
        ParseurWiki().feed(page)


if __name__ == "__main__":
    main()
