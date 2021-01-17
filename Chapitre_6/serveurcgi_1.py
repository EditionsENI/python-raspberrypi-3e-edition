#!/usr/bin/env python3
from http.server import CGIHTTPRequestHandler
from http.server import HTTPServer
import sys
import os


ip = "127.0.0.1"
port = 8080
repertoire = "/home/pi/www"


def main():
    try:
        os.chdir(repertoire)
        serveur = HTTPServer((ip, port), CGIHTTPRequestHandler)
        print(f"Démarrage du serveur CGI: http://{ip}:{port}")
        serveur.serve_forever()
    except FileNotFoundError as e:
        sys.stderr.write(f"ERREUR! Le répertoire \"{repertoire}\" n'existe pas!\n")
        raise e
    except KeyboardInterrupt:
        serveur.socket.close()


if __name__ == "__main__":
    main()
