#!/usr/bin/env python3
import cgi


formulaire = cgi.FieldStorage()
personne = ""
if "nom" in formulaire:
    personne = "Bonjour {} !".format(formulaire["nom"].value))
else:
    personne = "Mais qui &ecirc;tes-vous !?"


print("Content-Type: text-html; charset=utf-8\r\n\r\n")
html = f"""
<html>
<head>
<title>Exemple #3: Soumettre des formulaires avec la methode POST</title>
</head>
<body>
  <h1>Deuxieme &eacute;tape</h1>
  <p>{personne}<p>
</body>
</html>"""
print(html)
