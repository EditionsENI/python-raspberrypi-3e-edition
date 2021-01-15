#!/usr/bin/env python3
import requests
url = "https://fr.wikipedia.org/wiki/France"


def main():
    with requests.Session() as session:
        reponse = session.get(url)
        page = reponse.text
        with open("france.html", "w", encoding="UTF-8") as f:
            print(f"Sauvegarde la page {url} dans le fichier france.html.")
            f.write(page)


if __name__ == "__main__":
    main()
