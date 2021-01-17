#!/usr/bin/env python3
import email.utils
import datetime
import smtplib


serveursmtp = "smtp.free.fr"


From = "Patrice Clement <foo@bar.local>"
To = "Patrice Clement <foo@bar.local>"
Subject = "Le sujet de cet email."
Date = email.utils.formatdate()
Now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f"))


entetes = f"""From: {From}
To: {To}
Date: {Date}
Subject: {Subject}"""

corps = f"""{entetes}
Ceci est un test. Date du message: {now}
"""


def main():
    print("Envoi du courriel...")
    serveur = smtplib.SMTP(serveursmtp)
    serveur.set_debuglevel(1)
    erreur = serveur.sendmail(From, To, corps)
    serveur.quit()
    if erreur:
        print("Erreur! ", erreur)
    else:
        print("OK!")


if __name__ == "__main__":
    main()
