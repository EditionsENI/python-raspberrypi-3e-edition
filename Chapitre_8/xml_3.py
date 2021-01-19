#!/usr/bin/env python3
from xml.etree import ElementTree


def main():
    fichier = "bdd/commandes.xml"
    with open(fichier, "r", encoding="UTF-8") as f:
        arbre = ElementTree.parse(f)
        racine = arbre.getroot()
    commandes = racine.find("commandes")
    attributs = {"code": "LE40", "quantite": "5"}
    commande = ElementTree.SubElement(commandes, "commande", attrib=attributs)
    commande.text = "Lenovo X200"
    print("Ajout d'une nouvelle commande: {}".format(
        ElementTree.tostring(commande).decode("UTF-8")
    )
    arbre.write(fichier, encoding="UTF-8", xml_declaration=True)
    print("OK!")


if __name__ == "__main__":
    main()
