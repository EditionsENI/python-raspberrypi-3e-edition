#!/usr/bin/env python3
from flask import Flask


app = Flask(__name__)


@app.route("/")
def dit_hello():
    return "Hello World!"


@app.route("/user/<utilisateur>")
def affiche_utilisateur(utilisateur):
    return f"Bonjour {utilisateur} ! Comment allez vous ?"


@app.route("/id/<int:numero>")
def affiche_id(numero):
    return f"Identifiant #{numero}"


@app.route("/path/<path:souschemin>")
def affiche_souschemin(souschemin):
    return f"Quel est le sous-chemin ? {souschemin}"


if __name__ == "__main__":
    app.run()
